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

## 2. Model identity rule

The four model slots are deliberately frozen as **M1–M4** until execution because model availability, exact model identifiers and provider versions can change over time.

Immediately before execution, each slot must be mapped to an exact publicly identifiable model/version and recorded here in a commit **before the first primary run**.

No model may be substituted after primary data collection begins. If a model becomes unavailable before completion, the affected cells are marked `UNAVAILABLE` and a replacement is treated as a new experimental condition, not silently substituted.

### Model slots

- **M1:** TBD — exact model ID/version to be frozen before execution
- **M2:** TBD — exact model ID/version to be frozen before execution
- **M3:** TBD — exact model ID/version to be frozen before execution
- **M4:** TBD — exact model ID/version to be frozen before execution

## 3. Generation parameters

The following parameters must be fixed before primary execution:

- temperature: **0** where supported;
- top_p: **provider default**, unless the model requires explicit configuration;
- seed: **fixed seed where supported**, otherwise `NOT_AVAILABLE`;
- tools: **disabled** unless a problem explicitly requires them;
- web browsing: **disabled**;
- external retrieval: **disabled**;
- system/developer instructions: identical across A/B/C for each model, except the condition-specific prompt content;
- conversation history: **none**;
- language: **Italian**;
- output format: plain text unless the problem requires a specified format.

If a provider does not expose one of these parameters, record `NOT_EXPOSED` rather than attempting to infer it.

## 4. Prompt controls

For every P01–P30:

- the problem statement is identical across A/B/C;
- the gold answer is never supplied to the model;
- B and C must contain substantively equivalent task information;
- B is optimized as a prompt without explicitly imposing the REA governance procedure;
- C explicitly derives the final request from Problema, Obiettivo, Vincoli, Criteri and Verifica;
- prompt length is recorded for every run;
- no condition may receive privileged external information.

## 5. Execution order

The 360 cells should be randomized before execution. The randomization list must be generated and committed before the first run.

Recommended cell identifier:

`Pxx-C-Mx`

Examples:

- `P01-A-M1`
- `P01-B-M1`
- `P01-C-M1`
- `P01-A-M2`
- `...`
- `P30-C-M4`

## 6. Required run record

Each primary run must record:

`run_id | problem_id | condition | model_slot | exact_model_id | model_version | timestamp_utc | temperature | top_p | seed | tools | prompt_chars | prompt_tokens_if_available | output_chars | output_tokens_if_available | prompt | output | status`

## 7. Integrity rules

1. Metadata must be frozen before primary execution.
2. Any post-freeze change receives a new version and cannot overwrite the original metadata.
3. A failed or unavailable run is recorded; it is not silently deleted.
4. Provider-side model updates discovered after execution must be documented.
5. Primary analysis must distinguish protocol deviations from valid observations.
6. Results must not be filtered according to whether they favour REA.

## 8. Statistical interpretation

The primary comparison is **C vs B**.

A > C versus A is not sufficient evidence for REA because A is intentionally a weaker baseline.

Model identity is treated as an experimental factor. A result that appears only on one model is not sufficient to establish cross-model robustness.

## 9. Freeze state

Current state:

**PROTOCOL FROZEN**  
**DATASET FROZEN**  
**MODEL IDENTITIES: TO BE FROZEN BEFORE EXECUTION**  
**PRIMARY EXECUTION: NOT STARTED**

The next required commit must replace M1–M4 `TBD` entries with exact model identifiers and freeze the execution order.
