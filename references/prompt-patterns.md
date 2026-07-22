# Prompt patterns

## Contents

1. Minimal task handoff
2. Repository or architecture work
3. Research and synthesis
4. Document transformation
5. Autonomous implementation
6. Prompt debugging
7. Context topology and worker handoffs

## 1. Minimal task handoff

Use for a bounded request with few inputs:

```text
<goal>
[Concrete outcome and why it matters.]
</goal>

<inputs>
[Authoritative material.]
</inputs>

<requirements>
[Only constraints that change the result.]
</requirements>

<deliverable>
[Exact artifact or answer.]
</deliverable>

<verification>
[Observable evidence of correctness.]
</verification>
```

Remove tags that do not add separation.

## 2. Repository or architecture work

Include:

- exact repository and target files;
- read-only inspection scope before edits;
- authoritative design documents and their precedence;
- whether to diagnose, edit, implement, or all three;
- dirty-worktree preservation;
- decisions already settled versus questions to decide;
- tests, reread, diff, or other evidence required;
- exact files to modify or create;
- final response that names outcomes rather than repeating artifacts.

Avoid prescribing every shell command. Tell Fable what evidence it must collect and which mutations are authorized.

## 3. Research and synthesis

Include:

- freshness window and source quality;
- primary-source preference;
- how to distinguish fact, source claim, estimate, and inference;
- conflict handling and uncertainty reporting;
- citation placement;
- output decision the research must enable.

Do not ask for “comprehensive research” without a stopping rule. Define coverage dimensions or a decision threshold.

## 4. Document transformation

Separate:

- content that is authoritative and must remain;
- structure or style that can change;
- facts requiring verification;
- omissions the model may fill versus must flag;
- target reader and action enabled;
- destination file and preservation rules.

When the source is long, place it before the final query or point Fable to the file rather than duplicating it into the prompt.

## 5. Autonomous implementation

Include:

- permission to make reversible in-scope edits;
- real pause conditions;
- tool-result evidence for progress;
- external state or compaction behavior;
- bounded retries and failure reporting;
- material completion and verification;
- scope-control instruction.

Add this pattern when useful:

```text
When you have enough information to act, act. Do not re-derive established facts or re-litigate settled decisions. Do not add features, cleanup, refactors, abstractions, or compatibility work beyond this request.
```

Add this completion guard for long tasks:

```text
Before ending, inspect your last paragraph. If it is only a plan, promise, or list of work not yet performed, perform that work now unless blocked by information or authority only the user can provide.
```

## 6. Prompt debugging

Diagnose failures against six causes:

1. wrong outcome or missing artifact;
2. executor/subject role confusion;
3. conflicting authorities or formats;
4. missing authorization boundary;
5. no observable verification;
6. excessive prescription that blocks adaptation.

Rewrite the smallest set of instructions that fixes the causal failure. Do not respond to every bad output by adding another permanent rule.

## 7. Context topology and worker handoffs

For long or tool-heavy work, define what belongs in each layer:

- **Main context**: goal, architecture, constraints, settled decisions, current plan, progress ledger, unresolved decisions, and acceptance evidence.
- **Durable state**: task contract, checkpoints, decisions, artifact paths, test results, and a compact handoff that can survive context reset or compaction.
- **Isolated worker context**: repository exploration, source collection, raw logs, alternative hypotheses, and independent verification whose intermediate detail is not needed by the main thread.
- **Deterministic layer**: permissions, schemas, contracts, validators, hooks, budgets, and irreversible-action gates.

Require each worker handoff to contain:

1. status: complete, blocked, or needs decision;
2. concise findings or changes;
3. evidence and artifact pointers;
4. uncertainty, failed attempts, or conflicts that affect the parent;
5. the next decision or action, only when one is genuinely required.

Use a scheduler or direct parallel tool calls for homogeneous, independent operations that need no separate reasoning context. Use subagents when the work benefits from context isolation, distinct expertise, independent judgment, restricted permissions, or a fresh evaluator. Do not create one subagent per mechanical tool call.

For long loops, add a checkpoint rule rather than a fixed token threshold:

```text
Maintain a durable, information-dense checkpoint containing the goal, settled decisions, current state, artifact locations, verification results, and exact remaining work. Refresh it when the plan materially changes and before context compaction or handoff. Continue from the checkpoint; do not treat checkpoint creation as completion.
```
