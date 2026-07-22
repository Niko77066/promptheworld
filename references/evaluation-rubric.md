# Prompt evaluation rubric

Score each dimension 0–2. A paste-ready prompt should score at least 18/22 with no critical failure.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Outcome | Vague activity | Partial result | Concrete outcome and purpose |
| Executor vs subject | Confused | Implicit | Explicitly separated where relevant |
| Authority | Missing/conflicting | Some sources | Inputs and precedence are clear |
| Scope | Open-ended | Partial limits | Authorized work and exclusions are clear |
| Decisions | Re-litigates everything | Mixed | Settled decisions preserved; true choices framed |
| Autonomy | Stops constantly or acts without bounds | Uneven | Acts when sufficient; pauses only at real checkpoints |
| Deliverables | “Help/advice” | General format | Exact artifacts and destinations |
| Verification | Self-assertion | Generic review | Observable evidence, tests, or reread |
| Completion | Plan can masquerade as done | Partial | Material finish condition and early-stop guard |
| Fable fit | CoT/micro-rules/persona bloat | Mostly usable | Outcome-led, adaptive, evidence-grounded |
| Readability | Dense/repetitive | Understandable | Selective, structured, paste-ready |

## Critical failures

Reject or revise regardless of score when the prompt:

- contains a credential or asks the model to expose one;
- accidentally places Fable 5 inside the system being designed;
- grants destructive/external authority the user did not request;
- requests raw hidden reasoning or chain-of-thought extraction;
- gives contradictory deliverables or precedence;
- claims completion can be established by model self-report alone;
- instructs implementation when the user asked only for assessment.

## Final check

- Can a capable new colleague execute this without the missing conversation?
- Does every major section change the work or proof of completion?
- Could any instruction be removed without changing behavior?
- Are paths, URLs, names, and decisions preserved accurately?
- Is the final output contract shorter than the task itself?

