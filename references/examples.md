# Examples

## 1. Executor versus subject model

Raw request:

```text
Use Fable 5 to improve my agent spec. The agent only has Kimi K3 and GPT-5.6-sol. Decide whether to replace codex exec.
```

Essential correction:

```text
You are using Fable 5 to perform this architecture review. Fable 5 is not a production model available to the agent being designed. The subject agent may use only Kimi K3 and GPT-5.6-sol; do not add Fable 5 to its runtime or routing configuration.
```

Why: the executor's identity is contextual, not a product requirement.

## 2. Assessment versus implementation

Raw request:

```text
Look at this design and tell me whether it follows the architecture.
```

Polished boundary:

```text
Inspect the design and report evidence-backed findings. This is an assessment-only task: do not modify files or implement fixes. For each mismatch, cite the relevant file or diagram element and recommend one correction.
```

Why: Fable's autonomy needs an explicit mutation boundary.

## 3. End-to-end repository task

Raw request:

```text
Read these docs, research best practices, fix the spec, and make it good. Don't ask me too much.
```

Improved structure:

```text
<goal>
Rewrite [target file] into an implementation-ready specification that enables [purpose].
</goal>

<authorities>
Use [diagram] for power boundaries, [document] for skill governance, and current code for implemented behavior. When they conflict, distinguish a deliberate new decision from an accidental mismatch.
</authorities>

<scope>
You may inspect the repository and edit [target]. Preserve unrelated user changes. Do not implement runtime code.
</scope>

<execution>
Inspect the relevant files before editing. When enough information is available, act; do not stop after producing a plan. Pause only for an irreversible action, genuine scope expansion, or information only the user can provide.
</execution>

<deliverables>
Update [target] in place. Include decisions, migration, and verifiable acceptance criteria.
</deliverables>

<verification>
Reread the result, search for forbidden dependencies and contradictions, and report the file changed plus remaining user decisions.
</verification>
```

Why: the prompt supplies authority, scope, completion, and evidence without dictating private reasoning.

