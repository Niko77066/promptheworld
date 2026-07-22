# promptheworld

`promptheworld` is an agent skill for turning rough, overloaded, ambiguous, or underperforming requests into paste-ready prompts optimized for Fable 5 agent workflows.

It preserves the user's real intent while clarifying outcomes, authority, evidence, constraints, deliverables, verification, autonomy, context ownership, and stopping conditions.

## Triggers

Use the skill for requests such as:

- `打磨 prompt：…`
- `升级 prompt：…`
- `优化提示词`
- `改成 Fable 5 prompt`
- `promptheworld`
- auditing or debugging an underperforming Fable 5 prompt

## What it does

- distinguishes the executor model from the system or models being designed;
- converts notes, conversations, specs, files, and URLs into executable job handoffs;
- adds evidence, authorization, completion, verification, and handoff rules only when needed;
- designs context topology for long-running work without mechanically spawning subagents;
- keeps deterministic guards in contracts, hooks, validators, and permission layers;
- rejects magic phrases, raw chain-of-thought requests, embedded secrets, and unsupported completion claims.

## Install

With the Vercel agent-skills CLI:

```bash
npx skills add https://github.com/Niko77066/promptheworld
```

Or copy this repository into an agent skills directory so that `SKILL.md` is at the skill root.

## Contents

```text
promptheworld/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── evaluation-rubric.md
│   ├── examples.md
│   ├── fable5-official-guidance.md
│   ├── prompt-patterns.md
│   └── x-practitioner-notes.md
└── scripts/lint_prompt.py
```

The bundled linter is heuristic. It helps detect prompt debt and accidental secrets, but the evaluation rubric remains the final quality check.
