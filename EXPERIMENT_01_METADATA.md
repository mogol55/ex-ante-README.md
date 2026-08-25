# REA v0.1 — Experiment 01 Metadata

**Status:** FROZEN BEFORE EXECUTION  
**Date:** 2026-08-25  
**Dataset:** DATASET_01  
**Design:** 30 problems × 3 conditions × 4 model families = 360 primary runs

## 1. Experimental matrix

| Dimension | Fixed value |
|---|---|
| Problems | P01–P30 |
| Conditions | A Control / B Prompt Engineering / C REA |
| Model slots | M1 / M2 / M3 / M4 |
| Primary runs | 360 |
| Repetitions | 1 primary run per cell; repeats are secondary and must be labelled |
| Evaluation | blind, using DATASET_01 gold standards and preregistered metrics |

## 2. Frozen model identities

The four model families are fixed before primary execution to maximize cross-provider independence and reproducibility.

| Slot | Provider | Exact model ID | Role |
|---|---|---|---|
| M1 | OpenAI | `gpt-5-2025-08-07` | OpenAI reasoning/general model |
| M2 | Anthropic | `claude-sonnet-4-6` | Claude reasoning/general model |
| M3 | Google | `gemini-3.7-flash` | Gemini general/agentic model |
| M4 | Mistral AI | `mistral-large-2512` | Mistral general-purpose model |

These are exact model identifiers rather than moving aliases. OpenAI documents `gpt-5-2025-08-07` as an API snapshot; Anthropic documents `claude-sonnet-4-6` as a pinned 4.6 model ID; Google lists `gemini-3.7-flash` as a stable model; Mistral documents `mistral-large-2512` as Mistral Large 3.  

Primary execution must use these exact identifiers. A provider/model substitution is not permitted once data collection begins. If one becomes unavailable before completion, affected cells are marked `UNAVAILABLE`; a replacement becomes a separate model slot and is not silently substituted.

## 3. Generation parameters

The following parameters are fixed for primary execution:

- temperature: **0 where supported**;
- top_p: **provider default** unless the API requires a fixed value;
- seed: **fixed seed where supported**, otherwise `NOT_AVAILABLE`;
- reasoning/thinking: **disabled** where the provider permits disabling it; if the model requires reasoning internally, record that fact and do not attempt to expose or compare hidden reasoning;
- tools: **disabled**;
- web browsing/search: **disabled**;
- external retrieval: **disabled**;
- conversation history: **none**;
- language: **Italian**;
- output format: plain text unless the problem specifies another format.

If a provider does not expose a parameter, record `NOT_EXPOSED` rather than infer it.

## 4. Provider documentation references

- OpenAI model/API documentation: https://platform.openai.com/docs/models
- Anthropic model IDs and versioning: https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
- Google Gemini models: https://ai.google.dev/gemini-api/docs/models
- Mistral models: https://docs.mistral.ai/models/

## 5. Prompt controls

For every P01–P30:

- the problem statement is identical across A/B/C;
- the gold answer is never supplied to the model;
- B and C must contain substantively equivalent task information;
- B is optimized as a prompt without explicitly imposing the REA governance procedure;
- C explicitly derives the final request from Problema, Obiettivo, Vincoli, Criteri and Verifica;
- prompt length is recorded for every run;
- no condition may receive privileged external information.

## 6. Execution order

The 360 cells must be randomized before execution. The randomization list must be generated and committed before the first run.

Recommended cell identifier:

`Pxx-C-Mx`

Examples:

- `P01-A-M1`
- `P01-B-M1`
- `P01-C-M1`
- `P01-A-M2`
- `...`
- `P30-C-M4`

## 7. Required run record

Each primary run must record:

`run_id | problem_id | condition | model_slot | exact_model_id | model_version | timestamp_utc | temperature | top_p | seed | reasoning_mode | tools | prompt_chars | prompt_tokens_if_available | output_chars | output_tokens_if_available | prompt | output | status`

## 8. Integrity rules

1. Metadata must be frozen before primary execution.
2. Any post-freeze change receives a new version and cannot overwrite the original metadata.
3. A failed or unavailable run is recorded; it is not silently deleted.
4. Provider-side model updates discovered after execution must be documented.
5. Primary analysis must distinguish protocol deviations from valid observations.
6. Results must not be filtered according to whether they favour REA.

## 9. Statistical interpretation

The primary comparison is **C vs B**.

A > C versus A is not sufficient evidence for REA because A is intentionally a weaker baseline.

Model identity is treated as an experimental factor. A result that appears only on one model is not sufficient to establish cross-model robustness.

## 10. Freeze state

**PROTOCOL FROZEN**  
**DATASET FROZEN**  
**MODEL IDENTITIES FROZEN: M1–M4**  
**PRIMARY EXECUTION: NOT STARTED**

Next step: generate and commit the randomized 360-cell execution order, then run the matrix without changing the protocol.
