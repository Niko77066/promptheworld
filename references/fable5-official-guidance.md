# Fable 5 official guidance

Use this reference for model-specific behavior. Prefer the official sources below over community prompt recipes.

## Sources checked

- [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5), checked 2026-07-22.
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), checked 2026-07-22.
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort), checked 2026-07-22.
- [Task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets), checked 2026-07-22.

## Behavior that changes prompt design

### Strong instruction following

Fable 5 usually needs fewer behavioral enumerations than older models. One clear boundary can replace a long blacklist. Prefer a general decision rule plus evidence-based acceptance criteria.

### Long turns and high autonomy

Hard requests can run for many minutes or much longer. The caller should support streaming, longer timeouts, asynchronous progress, cancellation, and external state. The task prompt should prevent overplanning and tell Fable to act once enough information is available.

### Effort

Effort is the main intelligence/latency/cost control. Start at `high` for substantial prompt execution, use `xhigh` for the most capability-sensitive long-horizon work, and lower it for routine work. Effort changes tool-use behavior as well as prose. It is not a strict token budget.

Fable 5 uses adaptive thinking and does not accept manual thinking token budgets. Do not paste obsolete `budget_tokens` advice into prompts or callers.

### Scope control

At high effort, Fable may inspect or improve more than requested. State the authorized mutation boundary and forbid unrelated features, refactors, abstractions, defensive backups, and speculative compatibility work.

### Evidence-grounded progress

Require progress claims to point to current-session tool results or inspectable artifacts. Require failed or skipped work to be reported plainly. This is more reliable than asking the model to be honest in the abstract.

### Early stopping

In long autonomous work, Fable can occasionally end on a statement of intent. Define material completion and add a final check: a plan, promise, or next-step list is not completion when execution was requested.

### Context and memory

If the harness compacts context or provides external memory, tell Fable explicitly. Store durable state in files or memory, continue after compaction, and avoid surfacing a dwindling context counter that encourages premature wrap-up.

Use a memory system for confirmed reusable lessons, not task state already present in the repository. Keep one lesson per entry, update rather than duplicate, and delete lessons shown to be wrong.

### Subagents

Fable 5 delegates readily. Give positive criteria for delegation and prevent mechanical fan-out. Prefer independent subtasks, isolated evaluation, or long-lived specialists. Homogeneous tool calls usually belong in a bounded tool scheduler rather than one subagent per call.

### User communication

For long asynchronous harnesses, a dedicated send-to-user tool can carry user-facing content without ending the run. Do not route private reasoning or routine narration through it. Final summaries should re-ground the user: outcome first, then evidence and any decision needed.

### Reasoning output

Do not ask for raw internal reasoning or hidden chain-of-thought. Ask for conclusions, decision records, cited evidence, test results, and concise rationale. If the API returns thinking blocks, preserve them according to the API contract rather than transforming or extracting them through the task prompt.

## Prompt consequences

A strong Fable 5 task prompt usually contains:

1. the larger purpose and concrete outcome;
2. authoritative inputs and precedence;
3. decisions already made;
4. action and mutation boundaries;
5. acceptance evidence;
6. real user checkpoints;
7. material completion conditions;
8. a compact final-response contract.

It usually does not need a persona biography, a manual chain-of-thought recipe, dozens of micro-rules, or a complete plan that prevents the model from adapting to evidence.

