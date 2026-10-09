# Assignment 1 — AI prompt and output log

This log starts with the new assignment run. Each entry records the user's prompt verbatim, the generated content, and the assistant's final response. Student corrections can be added separately when made.

## Prompt 1 — user

> create new two new files: AI_appendix.md, and assignment.md in /home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1. AI_appendix is for my prompts and your raw outputs. assignment.md is where i do my assignment.

## Raw output 1 — assistant

Created [AI_appendix.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/AI_appendix.md) and [assignment.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md). The assignment file contains only a title; this prompt and response are recorded in the appendix.

## Prompt 2 — user

> Write A one-page test plan section: scope in and out, approach, entry and exit criteria, top three product risks.

## Raw output 2 — generated test plan section

### 1. Test plan — money transfer feature

**Basis and status.** This plan uses the Week 3 transfer brief and my HW3 test design. It is a proposed plan; no test execution or release approval is claimed.

**Scope in.** Test whole-tenge transfers from **100 to 500,000 KZT**; the **1,000,000 KZT** daily limit and its midnight reset in **Almaty time**; the SMS requirement **above 100,000 KZT**; six-digit code validity for **120 seconds**; cancellation after **three wrong codes**; and the rule that the amount error is shown when both amount and daily-limit rules fail. Include valid and invalid inputs, boundary values, combined conditions, and SMS state changes.

**Scope out.** This plan does not assess load/performance, accessibility, visual design, localisation, security penetration, or the reliability of the external SMS provider. Those need separate plans if they are release risks. The brief also leaves insufficient balance, code resend, duplicate confirmation, and transfers spanning midnight unclear; record these as requirement questions rather than assuming behaviour.

**Approach.** Use black-box equivalence partitions and **2-/3-value boundary analysis** for amount and time limits, a decision table for amount × daily total × SMS threshold, and a state table for correct/wrong/expired codes. Run independent manual cases in a test environment with resettable accounts and daily totals, a captured SMS inbox, and a controllable clock. Link every case and result to its requirement. Add regression checks after any fix.

**Entry criteria.** A versioned build is deployed and passes smoke checks; transfer rules and expected outcomes are agreed; test accounts, balances, recipient, daily totals, SMS capture, and time control are available. Mark a case *blocked* if its prerequisite is missing.

**Exit criteria.** All planned cases have recorded pass/fail/blocked results; every stated requirement has linked test evidence; no critical or high-severity defect remains open; amount/daily-limit boundaries and required SMS transitions pass. List untested behaviour and unresolved requirement questions as residual risks, with written acceptance by the release decision-maker before release.

**Top three product risks.** (1) An invalid amount or daily-limit bypass moves too much money. (2) SMS approval is bypassed, expires incorrectly, or allows repeated confirmation. (3) A wrong Almaty-time midnight reset miscalculates the daily total.

## Raw output 2 — assistant final response

Added the one-page test plan to [assignment.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md). The prompt, generated section, and this response are recorded in [AI_appendix.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/AI_appendix.md).

## Prompt 3 — user

> I have a HW3 file, can you please write me 12 test cases from there, and I will continue to write it in full format, and tracing to a requirement. Just write me down the cases I need to check

## Raw output 3 — generated case ideas

### 2. Twelve test cases to develop from HW3

These are **case ideas only**. Add the full case fields and requirement links yourself.

1. **TC-01 — Below minimum:** Submit **99 KZT**; check that the amount is rejected. *(HW3 AMOUNT-01)*
2. **TC-02 — Minimum valid amount:** Submit **100 KZT**; check that it proceeds without SMS approval. *(HW3 AMOUNT-02)*
3. **TC-03 — At SMS threshold:** Submit **100,000 KZT**; check that no SMS code is required. *(HW3 AMOUNT-03)*
4. **TC-04 — First amount above SMS threshold:** Submit **100,001 KZT**; check that a six-digit SMS code is requested. *(HW3 AMOUNT-04)*
5. **TC-05 — Maximum valid amount:** Submit **500,000 KZT**; check that the amount is accepted and SMS approval is requested. *(HW3 AMOUNT-05)*
6. **TC-06 — Above maximum:** Submit **500,001 KZT**; check that the amount is rejected. *(HW3 AMOUNT-06)*
7. **TC-07 — Two limits fail:** Set today's transfer total to **900,000 KZT**, then submit **500,001 KZT**; check that the **amount error** is shown before the daily-limit error. *(HW3 decision table, R5–R8)*
8. **TC-08 — Daily limit fails:** Set today's total to **950,000 KZT**, then submit **100,000 KZT**; check that the **daily-limit error** is shown. *(HW3 decision table, R3–R4)*
9. **TC-09 — Correct SMS code first:** Submit **100,001 KZT** and enter the correct code on the first attempt; check that the transfer is confirmed. *(HW3 TEST-01)*
10. **TC-10 — Correct SMS code third:** Submit **100,001 KZT**, enter two wrong codes, then the correct code before expiry; check that the transfer is confirmed. *(HW3 TEST-03)*
11. **TC-11 — Three wrong SMS codes:** Submit **100,001 KZT** and enter three wrong codes; check that the transfer is blocked/cancelled. *(HW3 TEST-07)*
12. **TC-12 — SMS code expires:** Submit **100,001 KZT**, enter two wrong codes, then let more than **120 seconds** pass; check that the transfer expires/cancels. *(HW3 TEST-06)*

## Raw output 3 — assistant final response

Added 12 short case ideas from HW3 to [assignment.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md). I left the full test-case format and requirement tracing for you. Your prompt and the generated list are recorded in [AI_appendix.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/AI_appendix.md).

## Prompt 4 — user (interrupted)

> Can you check my edits? in assignment.md I added Tracing, Precondition, steps,

No assistant output was produced for this interrupted prompt.

## Prompt 5 — user

> Can you check my edits? in assignment.md I added Tracing, Precondition, steps, expected, postconditions for the first test case. What to write in traces field? What is REQ-0.1 in slides?

## Raw output 5 — assistant final response

Your first case has the right fields. `REQ-0.1` is not defined in the Week 3 or Week 4 slides. Week 4 slide 17 uses `REQ-3.1` as an example for “Amount 100–500,000.” These slide IDs are examples, so choose an ID such as `REQ-01`, define it in a requirement list, and use it consistently in the case and traceability matrix. For TC-01, write `Traces to: REQ-01 — transfer amount must be a whole number from 100 to 500,000 KZT inclusive.`

`PRECON1` is a good start, but add the logged-in test account and make the source/recipient accounts available; TC-07 and TC-08 will need daily-total overrides. Your expected result and postcondition are clear. Expand `Steps: Transfer of 99 KZT` into repeatable actions: open Transfers, select accounts, enter 99 KZT, tap Continue. I left `assignment.md` unchanged.

### **WHAT WAS CHANGED AT THE MOMENT?**

I added requirements list and specified them in "trace" field. I also added "Tracing", "Preconditions", "Steps", "Expected", "Postconditions" as they need for completing traceability matrix. for each test case Also AI agent recommended me to add a logged in account as an example, but I decided to not to as it was not required. Also it suggested me to write more details of the steps to repeatable actions.



## Prompt 6 — user

> I have done the 2. Twelve test cases from your week 3 design work, in full format, each traced to a requirement. Can you validate correctness?

## Raw output 6 — assistant final response

Not yet fully correct: TC-08 conflicts with itself, and TC-10–12 are still placeholders. The other selected scenarios largely match HW3.

- [TC-08](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:118): its title says **100,000 KZT** with a 950,000 KZT daily total, but its steps submit **500,001 KZT**. At 500,001, both limits fail, so REQ-06 requires the **amount error**, not the expected daily-limit error. Use 100,000 in the steps.
- [TC-10–12](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:142): tracing, preconditions, steps, expected results, and postconditions are blank. They do not yet meet the “12 cases in full format” requirement.
- [TC-03](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:58): add **REQ-03** to its trace; this case checks the no-SMS side of the 100,000 KZT threshold, not only amount validity.
- [REQ-02](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:28): include the brief's **midnight reset in Almaty time**. None of these 12 cases checks that part, so mark its coverage as partial in the later matrix.
- [PRECON1](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:21): it says daily total **0**, while TC-07/08 need **900,000/950,000**. Write “PRECON1 except daily total = …” for those cases. Also identify a test source/recipient and access to SMS and time control where needed; fictional test IDs are fine, but a colleague needs a reproducible starting state.
- [Steps](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:40): “Select card; Transfer 99 KZT” does not say which recipient or which action triggers validation. Spell out selection, amount entry, and submission. For TC-09, choose a specific entry time such as **30 seconds after code issue** rather than “within 120 seconds.”
- [TC-06](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:94): finish the expected-result sentence (“no SMS approval is requested; no debit occurs”).

TC-01/02/04/05/07/09 have the right core behaviour, and the balance arithmetic in TC-02/03/09 is correct. I left `assignment.md` unchanged; this review is recorded in [AI_appendix.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/AI_appendix.md).



### **WHAT WAS CHANGED AT THE MOMENT?**

I corrected some parts according to AI agents notes.

## Prompt 7 — user

> I added 3. A Traceability Matrix. Help me to fill Technique Status columns

## Raw output 7 — generated matrix columns

| Requirement / gap | Linked cases | Technique | Status |
| --- | --- | --- | --- |
| REQ-01 Transfer amount is a whole number of KZT from **100 through 500,000**. | TC-01 - TC-08 | Equivalence partitioning + 2-value BVA + decision table | Designed, not run; partial: fractional/empty/non-numeric inputs not covered |
| REQ-02 The total of transfers in a day must not exceed **1,000,000 KZT**. Resets at midnights | TC-02, TC-07, TC-08 | Equivalence partitioning + decision table | Designed, not run; partial: exact limit and midnight reset not covered |
| REQ-03 Transfers **above 100,000 KZT** require a **six-digit SMS code**. | TC-03 - TC-05, TC-09 - TC11 | 2-value BVA at 100,000/100,001 + state transition | Designed, not run; threshold and six-digit issuance covered by cases |
| REQ-04 The SMS code is valid for **120 seconds**. | TC-09, TC-12 | State transition testing + timing check | Designed, not run; partial: exact 120-second boundary not covered |
| REQ-05 **Three wrong code attempts** cancel the transfer. | TC-10 - TC-12 | State transition testing | Designed, not run; TC-11 checks the third wrong code, but TC-12's steps omit the two wrong codes named in its title |
| REQ-06 If amount and daily-limit rules are both violated, show the **amount error**. | TC-07 | Decision table (combined conditions / error precedence) | Designed, not run; combined-error outcome covered by TC-07 |
| GAP-01 insufficient balance | — | — | NOT COVERED |
| GAP-02 cancelled/expired transfer and daily total | — | — | NOT COVERED |
| GAP-03 duplicate confirmation/debit | — | — | NOT COVERED |

**Status note:** These are design-coverage statements. No case has been executed, so none can be marked passed or failed yet.

## Raw output 7 — assistant final response

Filled the Technique and Status columns in [assignment.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:180). Every status distinguishes **designed** from **executed**; none claims a pass. I marked REQ-01, REQ-02, and REQ-04 as partially covered and corrected `TC-12s` to `TC-12`.

Three details to check in your own text: [TC-03](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:58) is linked to REQ-03 in the matrix but its own trace lists only REQ-01; [TC-12](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:166) says “two wrong codes” in its title but its steps do not enter them; and [REQ-02](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/assignment.md:185) should say “resets at midnight Almaty time.” Your prompt and the generated matrix are recorded in [AI_appendix.md](/home/az1tchhh/Documents/University/KBTU/SoftwareTesting/assignments/Assignment_1/AI_appendix.md).

