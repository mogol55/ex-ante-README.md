#!/usr/bin/env python3
"""REA Experiment 01 deterministic runner.

Generates the frozen 360-cell execution matrix and, when provider SDKs/keys are
available, executes cells through provider adapters. No agents, web search,
tools, retrieval, or conversation memory are used.

The runner never reads or sends gold answers to models.
"""
from __future__ import annotations

import csv
import json
import os
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results_01.jsonl"
ORDER = ROOT / "RUN_ORDER_01.csv"
PROMPTS = ROOT / "PROMPTS_01.jsonl"
SEED = 20260825
MODELS = {
    "M1": ("openai", "gpt-5-2025-08-07"),
    "M2": ("anthropic", "claude-sonnet-4-6"),
    "M3": ("google", "gemini-3.7-flash"),
    "M4": ("mistral", "mistral-large-2512"),
}
CONDITIONS = ("A", "B", "C")
PROBLEMS = tuple(f"P{i:02d}" for i in range(1, 31))


def matrix():
    cells = [
        (p, c, m) for p in PROBLEMS for m in MODELS for c in CONDITIONS
    ]
    rng = random.Random(SEED)
    rng.shuffle(cells)
    return [(i + 1, p, c, m, f"{p}-{c}-{m}") for i, (p, c, m) in enumerate(cells)]


def write_order():
    rows = matrix()
    if ORDER.exists():
        with ORDER.open("r", encoding="utf-8", newline="") as f:
            existing = list(csv.DictReader(f))
        expected = [r[4] for r in rows]
        actual = [r["cell_id"] for r in existing]
        if actual != expected:
            raise SystemExit("RUN_ORDER_01.csv exists but does not match frozen seed/matrix")
        return rows
    with ORDER.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["order", "problem_id", "condition", "model_slot", "cell_id"])
        w.writerows(rows)
    return rows


def load_prompts():
    if not PROMPTS.exists():
        raise SystemExit(
            "PROMPTS_01.jsonl is required. It must contain exactly 90 records "
            "(30 problems x 3 conditions) and must be frozen before execution."
        )
    records = {}
    with PROMPTS.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            x = json.loads(line)
            key = (x["problem_id"], x["condition"])
            if key in records:
                raise SystemExit(f"Duplicate prompt: {key}")
            if key[0] not in PROBLEMS or key[1] not in CONDITIONS:
                raise SystemExit(f"Invalid prompt key: {key}")
            records[key] = x["prompt"]
    if len(records) != 90:
        raise SystemExit(f"Expected 90 prompts, found {len(records)}")
    return records


def call_model(provider, model, prompt):
    """Provider adapter. Returns text and provider metadata.

    SDK imports are local so the matrix can still be generated without all
    provider packages installed. The execution environment must provide the
    corresponding API key through environment variables.
    """
    if provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        r = client.responses.create(model=model, input=prompt, tools=[])
        return r.output_text, {"provider_request_id": getattr(r, "id", None)}

    if provider == "anthropic":
        from anthropic import Anthropic
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        r = client.messages.create(model=model, max_tokens=2048, messages=[{"role": "user", "content": prompt}])
        text = "".join(getattr(b, "text", "") for b in r.content if getattr(b, "type", None) == "text")
        return text, {"provider_request_id": getattr(r, "id", None)}

    if provider == "google":
        from google import genai
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        r = client.models.generate_content(model=model, contents=prompt)
        return r.text, {"provider_request_id": None}

    if provider == "mistral":
        from mistralai import Mistral
        client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
        r = client.chat.complete(model=model, messages=[{"role": "user", "content": prompt}], temperature=0)
        return r.choices[0].message.content, {"provider_request_id": getattr(r, "id", None)}

    raise ValueError(provider)


def main(execute=False):
    rows = write_order()
    print(f"Frozen matrix: {len(rows)} cells")
    if not execute:
        print(f"Execution disabled. Order written to {ORDER}")
        return

    prompts = load_prompts()
    existing = set()
    if OUT.exists():
        with OUT.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    existing.add(json.loads(line)["cell_id"])

    with OUT.open("a", encoding="utf-8") as out:
        for order, problem, condition, slot, cell_id in rows:
            if cell_id in existing:
                continue
            provider, model = MODELS[slot]
            prompt = prompts[(problem, condition)]
            started = datetime.now(timezone.utc).isoformat()
            try:
                text, meta = call_model(provider, model, prompt)
                status = "OK"
                error = None
            except Exception as exc:
                text = ""
                meta = {}
                status = "ERROR"
                error = f"{type(exc).__name__}: {exc}"
            record = {
                "run_id": f"R{order:03d}", "cell_id": cell_id,
                "problem_id": problem, "condition": condition,
                "model_slot": slot, "exact_model_id": model,
                "provider": provider, "timestamp_utc": started,
                "temperature": 0, "top_p": "PROVIDER_DEFAULT",
                "seed": "NOT_AVAILABLE_UNLESS_PROVIDER_EXPOSES_FIXED_SEED",
                "tools": "DISABLED", "web": "DISABLED", "retrieval": "DISABLED",
                "conversation": "NONE", "prompt_chars": len(prompt),
                "prompt": prompt, "output": text, "status": status,
                "error": error, **meta,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()


if __name__ == "__main__":
    main(execute="--execute" in sys.argv)
