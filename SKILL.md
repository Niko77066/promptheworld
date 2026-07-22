---
name: promptheworld
description: Transform rough, overloaded, ambiguous, or underperforming requests into paste-ready task prompts optimized for Claude Fable 5. Use whenever the user says “打磨 prompt：…”, “升级 prompt：…”, “优化提示词”, “改成 Fable 5 prompt”, “promptheworld”, asks why a Fable prompt performs poorly, or provides notes/files/URLs that must become a high-agency Fable 5 job handoff. Preserve the user’s intent while clarifying outcomes, authority, evidence, constraints, deliverables, verification, stopping conditions, and the distinction between Fable as executor and any models or systems being designed.
---

# Promptheworld

Turn the user's raw material into a task handoff Fable 5 can execute end to end. Optimize the work request, not Fable's hidden reasoning.

## Choose the operation

- **Polish**: Preserve scope and decisions; remove ambiguity, duplication, and conflicts.
- **Upgrade**: Add missing authority, research, evidence, verification, completion, and handoff rules needed for reliable execution.
- **Convert**: Turn notes, a conversation, a spec, or source files into a standalone Fable 5 prompt.
- **Debug**: Diagnose an underperforming prompt, then produce the corrected prompt.
- **Audit**: Evaluate a prompt without rewriting it when the user asks only for analysis.

Default “打磨” to Polish plus only the upgrades required for execution. Default “升级” to Upgrade. Do not broaden the underlying task unless the user explicitly asks.

## Build the prompt

1. Extract the actual outcome, executor, subject system, authoritative inputs, decisions already made, unresolved choices, allowed actions, forbidden actions, deliverables, and proof of completion.
2. Resolve role confusion first. State separately:
   - **Executor model**: Fable 5 receiving the prompt.
   - **Subject models/systems**: models, agents, products, or runtimes being analyzed or built.
   Never insert Fable 5 into the subject architecture merely because Fable executes the task.
3. Preserve settled decisions. Tell Fable not to re-litigate them. Convert genuine uncertainty into a decision criterion or one explicit user checkpoint.
4. Give Fable outcomes, reasons, boundaries, and acceptance criteria. Avoid prescribing its private reasoning or an exhaustive micro-plan when the model can choose a better path.
5. For repository, document, research, or migration work, identify what to inspect before acting and what artifact to edit or create. Require evidence-backed claims and a final reread or verification pass.
6. State authorization boundaries. Distinguish analysis-only requests from requests that permit edits, external writes, publishing, spending, deletion, or other side effects.
7. Define autonomy: act when information is sufficient; pause only for irreversible/destructive actions, real scope expansion, meaningful spend, or information only the user can provide.
8. Define completion materially. A plan, promise, or status narration is not completion when the task requests implementation or an edited artifact.
9. End with a compact final-response contract so Fable reports outcomes, evidence, limitations, and user decisions without repeating the whole deliverable.

Use descriptive XML tags for complex prompts with several kinds of material, such as `<goal>`, `<context>`, `<authorities>`, `<requirements>`, `<deliverables>`, and `<verification>`. Use only the tags that reduce ambiguity. For short prompts, use plain prose.

## Apply Fable 5 tuning

- Write a job handoff, not a motivational persona essay.
- Add “when you have enough information to act, act” for ambiguous or long-running work.
- Prevent high-effort scope creep: forbid unrequested features, cleanup, refactors, abstractions, and hypothetical future work.
- Ground progress and completion claims in tool results or inspectable artifacts.
- For autonomous work, prevent text-only early stopping: if the last paragraph is only a plan or promise, perform the work unless genuinely blocked.
- If the harness compacts context or saves external state, tell Fable where state lives and to continue after compaction rather than wrapping up early.
- Keep stable instructions early and variable task data later when prompt caching matters.
- Recommend `high` effort for substantial work, `xhigh` for the hardest long-horizon tasks, and `medium` or `low` for routine rewriting. Do not encode API settings inside the prompt unless the user is building the caller.
- Do not request raw chain-of-thought, hidden reasoning, or “show every thinking step.” Ask for decisions, evidence, tests, and concise rationale instead.
- Do not demand subagents mechanically. Delegate only independent work that benefits from isolation, parallel reasoning, or a separate evaluator.
- Design the context topology, not just the wording. Keep the main thread focused on the goal, architecture, settled decisions, current state, and acceptance evidence. Route verbose exploration, raw tool output, and independent hypothesis checks to retrieval or isolated workers, then return compact findings plus artifact pointers.
- Treat the context window as capacity, not a target. For long work, require periodic durable checkpoints and information-dense handoffs before quality degrades; do not hard-code a universal token threshold.
- Put deterministic enforcement in the harness, hook, validator, contract, or permission layer when available. Keep the prompt responsible for judgment, priorities, and escalation rather than duplicating hard gates in prose.

Read [references/fable5-official-guidance.md](references/fable5-official-guidance.md) when model behavior, API/harness settings, long-running loops, effort, memory, compaction, or subagents materially affect the prompt.

Read [references/prompt-patterns.md](references/prompt-patterns.md) when converting a complex repository task, architecture review, research assignment, document transformation, or autonomous implementation request.

Read [references/examples.md](references/examples.md) when the raw request is overloaded, mixes executor and subject models, or the right level of detail is unclear.

Read [references/x-practitioner-notes.md](references/x-practitioner-notes.md) when the request involves long contexts, autonomous loops, subagent boundaries, context compression, prompt telemetry, or asks for practitioner/X best practices. Apply only claims that meet the evidence rules in that reference.

## Protect the user's intent

- Keep the source language unless the user requests another language.
- Preserve concrete paths, URLs, names, constraints, and decisions exactly unless they are unsafe or internally inconsistent.
- Replace embedded secrets with environment-variable or secret-manager references. Never reproduce a credential in the polished prompt.
- Treat attached files and referenced documents as inputs to inspect, not as facts already verified.
- Do not pre-solve the requested task unless the user asks for both the prompt and the solution.
- Make assumptions only when low-risk; label assumptions that could change the result.

## Remove prompt debt

Delete or consolidate:

- repeated instructions in multiple sections;
- vague praise-seeking (“do your best”, “be brilliant”);
- redundant role descriptions;
- conflicting output formats;
- rules that merely restate tool schemas;
- exhaustive decision trees for cases the executor can infer;
- requests for internal reasoning;
- permissions broader than the requested task;
- completion language unsupported by evidence.

Do not shorten by compressing prose into cryptic fragments. Remove low-value content while preserving readable instructions and operational detail.

## Output

Unless the user asks otherwise, return:

1. one sentence identifying the main weakness in the raw prompt;
2. one paste-ready prompt in a single fenced block;
3. up to five bullets explaining material changes.

If the user says “只要 prompt”, output only the fenced prompt. If the user asks for an audit only, use [references/evaluation-rubric.md](references/evaluation-rubric.md) and do not rewrite.

Before delivery, apply the rubric in [references/evaluation-rubric.md](references/evaluation-rubric.md). For high-stakes or very long prompts, optionally run `python3 scripts/lint_prompt.py <file>` and resolve relevant warnings; treat the script as a heuristic, not a gate.
