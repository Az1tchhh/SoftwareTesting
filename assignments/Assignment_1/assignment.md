# Assignment 1

## 1. Test plan — money transfer feature

**Basis and status.** This plan uses the Week 3 transfer brief and my HW3 test design. It is a proposed plan; no test execution or release approval is claimed.

**Scope in.** Test whole-tenge transfers from **100 to 500,000 KZT**; the **1,000,000 KZT** daily limit and its midnight reset in **Almaty time**; the SMS requirement **above 100,000 KZT**; six-digit code validity for **120 seconds**; cancellation after **three wrong codes**; and the rule that the amount error is shown when both amount and daily-limit rules fail. Include valid and invalid inputs, boundary values, combined conditions, and SMS state changes.

**Scope out.** This plan does not assess load/performance, accessibility, visual design, localisation, security penetration, or the reliability of the external SMS provider. Those need separate plans if they are release risks. The brief also leaves insufficient balance, code resend, duplicate confirmation, and transfers spanning midnight unclear; record these as requirement questions rather than assuming behaviour.

**Approach.** Use black-box equivalence partitions and **2-/3-value boundary analysis** for amount and time limits, a decision table for amount × daily total × SMS threshold, and a state table for correct/wrong/expired codes. Run independent manual cases in a test environment with resettable accounts and daily totals, a captured SMS inbox, and a controllable clock. Link every case and result to its requirement. Add regression checks after any fix.

**Entry criteria.** A versioned build is deployed and passes smoke checks; transfer rules and expected outcomes are agreed; test accounts, balances, recipient, daily totals, SMS capture, and time control are available. Mark a case *blocked* if its prerequisite is missing.

**Exit criteria.** All planned cases have recorded pass/fail/blocked results; every stated requirement has linked test evidence; no critical or high-severity defect remains open; amount/daily-limit boundaries and required SMS transitions pass. List untested behaviour and unresolved requirement questions as residual risks, with written acceptance by the release decision-maker before release.

**Top three product risks.** (1) An invalid amount or daily-limit bypass moves too much money. (2) SMS approval is bypassed, expires incorrectly, or allows repeated confirmation. (3) A wrong Almaty-time midnight reset miscalculates the daily total.

## 2. Twelve test cases from your week 3 design work, in full format, each traced to a requirement.

Let us set a static precondition for all test cases for simplicity: Available balance 2000000 KZT; daily total 0 KZT. Let's call it **PRECON1**

Requirements list:

| ID     | Requirement                                                  |
| ------ | ------------------------------------------------------------ |
| REQ-01 | Transfer amount is a whole number of KZT from **100 through 500,000**. |
| REQ-02 | The total of transfers in a day must not exceed **1,000,000 KZT**. Resets at midnights |
| REQ-03 | Transfers **above 100,000 KZT** require a **six-digit SMS code**. |
| REQ-04 | The SMS code is valid for **120 seconds**.                   |
| REQ-05 | **Three wrong code attempts** cancel the transfer.           |
| REQ-06 | If amount and daily-limit rules are both violated, show the **amount error**. |

1. **TC-01 — Below minimum:** Submit **99 KZT**; check that the amount is rejected. *(HW3 AMOUNT-01)*

   Tracing:  REQ-01

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 99 KZT.

   Expected: Amount validation rejects the transfer as outside 100–500,000 KZT; no SMS approval starts; no debit occurs.

   Postcondition: No transfer; source balance 2,000,000 KZT; daily total 0.

2. **TC-02 — Minimum valid amount:** Submit **100 KZT**; check that it proceeds without SMS approval. *(HW3 AMOUNT-02)*

   Tracing:  REQ-01, REQ-02

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 100 KZT.

   Expected: Amount passes validation; transfer follows the no-SMS flow.

   Postcondition: source balance 1,999,900 KZT; daily total 100 KZT.

3. **TC-03 — At SMS threshold:** Submit **100,000 KZT**; check that no SMS code is required. *(HW3 AMOUNT-03)*

   Tracing: REQ-01, REQ-03

   Preconditions: PRECON1

   Steps:  1) Select card. 2) Transfer 100,000 KZT.

   Expected: Amount passes validation; transfer follows the no-SMS flow.

   Postcondition: source balance 1,900,000 KZT; daily total 100,000 KZT.

4. **TC-04 — First amount above SMS threshold:** Submit **100,001 KZT**; check that a six-digit SMS code is requested. *(HW3 AMOUNT-04)*

   Tracing: REQ-01, REQ-03;

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 100,001 KZT.

   Expected: Amount passes validation; a **six-digit** code is issued and the transfer waits for it

   Postcondition: Transfer pending; source balance 2,000,000 KZT; daily total 0.

5. **TC-05 — Maximum valid amount:** Submit **500,000 KZT**; check that the amount is accepted and SMS approval is requested. *(HW3 AMOUNT-05)*

   Tracing: REQ-01, REQ-03;

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 500,000 KZT.

   Expected: Amount passes validation; a six-digit SMS code is issued

   Postcondition: Transfer pending; source balance 2,000,000 KZT; daily total 0.

6. **TC-06 — Above maximum:** Submit **500,001 KZT**; check that the amount is rejected. *(HW3 AMOUNT-06)*

   Tracing: REQ-01

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 500,001 KZT.

   Expected: Amount validation rejects the transfer; no SMS approval is requested

   Postcondition: No transfer; source balance 2,000,000 KZT; daily total 0.

7. **TC-07 — Two limits fail:** Set today's transfer total to **900,000 KZT**, then submit **500,001 KZT**; check that the **amount error** is shown before the daily-limit error. *(HW3 decision table, R5–R8)*

   Tracing: REQ-01, REQ-02, REQ-06;

   Preconditions: PRECON1 + daily total 900,000 KZT

   Steps: 1) Select card. 2) Transfer 500,001 KZT.

   Expected: The **amount error** is shown, not the daily-limit error; no SMS or debit occurs.

   Postcondition: No transfer; source balance 2,000,000 KZT; daily total 900,000

8. **TC-08 — Daily limit fails:** Set today's total to **950,000 KZT**, then submit **100,000 KZT**; check that the **daily-limit error** is shown. *(HW3 decision table, R3–R4)*

   Tracing: REQ-01, REQ-02;

   Preconditions: PRECON1 + daily total 950,000 KZT

   Steps: 1) Select card. 2) Transfer 100,000 KZT.

   Expected: Daily-limit error is shown; transfer does not proceed and no debit occurs.

   Postcondition: No transfer; source balance 2,000,000 KZT; daily total 950,000 KZT.

9. **TC-09 — Correct SMS code first:** Submit **100,001 KZT** and enter the correct code on the first attempt; check that the transfer is confirmed. *(HW3 TEST-01)*

   Tracing: REQ-03, REQ-04;

   Preconditions: PRECON1

   Steps: 1) Select card. 2) Transfer 100,001 KZT. 3) Receive the code 4) Enter the code after 30 seconds

   Expected: Transfer is confirmed

   Postcondition: Source balance 1,899,999 KZT; daily total 100,001 KZT; transfer's confirmed.

10. **TC-10 — Correct SMS code third:** Submit **100,001 KZT**, enter two wrong codes, then the correct code before expiry; check that the transfer is confirmed. *(HW3 TEST-03)*

    Tracing: REQ-03, REQ-05;

    Preconditions: PRECON1

    Steps: 1) Select card. 2) Transfer 100,001 KZT. 3) Receive the code 4) Enter a wrong code 5) Enter a wrong code again 6) Enter the correct code within 120 seconds 

    Expected: The first two attempts are rejected; the third, correct attempt confirms the transfer once; no earlier debit occurs.

    Postcondition: Source balance 1,899,999 KZT; daily total 100,001 KZT; transfer confirmed.

11. **TC-11 — Three wrong SMS codes:** Submit **100,001 KZT** and enter three wrong codes; check that the transfer is blocked/cancelled. *(HW3 TEST-07)*

    Tracing: REQ-03, REQ-05;

    Preconditions: PRECON1

    Steps: 1) Select card. 2) Transfer 100,001 KZT. 3) Receive the code 4) Enter a wrong code 5) Enter a wrong code again 6) Enter a wrong code again

    Expected: After the third wrong entry, the transfer reaches **Blocked/cancelled**

    Postcondition: Transfer cancelled; source balance 2,000,000 KZT. Daily total unchanged

12. **TC-12 — SMS code expires:** Submit **100,001 KZT**, enter two wrong codes, then let more than **120 seconds** pass; check that the transfer expires/cancels. *(HW3 TEST-06)*

    Tracing: REQ-04, REQ-05;

    Preconditions: PRECON1

    Steps:  1) Select card. 2) Transfer 100,001 KZT. 3) Wait 121 seconds 4) Enter the code

    Expected: Code is expired; the pending transfer is cancelled

    Postcondition: Transfer expired/cancelled; source balance 2,000,000 KZT. Daily total unchanged



## 3. A Traceability Matrix.

| Requirement / gap                                            | Linked cases                | Technique                                         | Status      |
| ------------------------------------------------------------ | --------------------------- | ------------------------------------------------- | ----------- |
| REQ-01 Transfer amount is a whole number of KZT from **100 through 500,000**. | TC-01 - TC-08               | Equivalence partitioning + 2-value BVA + decision table | Designed, not run; partial: fractional/empty/non-numeric inputs not covered |
| REQ-02 The total of transfers in a day must not exceed **1,000,000 KZT**. Resets at midnights | TC-02, TC-07, TC-08         | Equivalence partitioning + decision table | Designed, not run; partial: exact limit and midnight reset not covered |
| REQ-03 Transfers **above 100,000 KZT** require a **six-digit SMS code**. | TC-03 - TC-05, TC-09 - TC11 | 2-value BVA at 100,000/100,001 + state transition | Designed, not run; threshold and six-digit issuance covered by cases |
| REQ-04 The SMS code is valid for **120 seconds**.            | TC-09, TC-12               | State transition testing + timing check | Designed, not run; partial: exact 120-second boundary not covered |
| REQ-05 **Three wrong code attempts** cancel the transfer.    | TC-10 - TC-12               | State transition testing | Designed, not run; TC-11 checks the third wrong code, but TC-12's steps omit the two wrong codes named in its title |
| REQ-06 If amount and daily-limit rules are both violated, show the **amount error**. | TC-07                       | Decision table (combined conditions / error precedence) | Designed, not run; combined-error outcome covered by TC-07 |
| GAP-01 insufficient balance                                  | —                           | —                                                 | NOT COVERED |
| GAP-02 cancelled/expired transfer and daily total            | —                           | —                                                 | NOT COVERED |
| GAP-03 duplicate confirmation/debit                          | —                           | —                                                 | NOT COVERED |



## 4. SMS-code release checklist (11 items)

Mark each item **pass, fail, blocked, or not run**, with a build and evidence link. Items marked `GAP` need a product decision before they can pass.

- [ ] At **100,000 KZT**, no SMS code is requested (REQ-03; TC-03).
- [ ] At **100,001 KZT**, a **six-digit** SMS code is requested (REQ-03; TC-04).
- [ ] No debit occurs while confirmation is pending (TC-04).
- [ ] Correct code before expiry confirms exactly one transfer (TC-09).
- [ ] Correct code on the third attempt still confirms (TC-10).
- [ ] Third wrong code cancels the transfer (REQ-05; TC-11).
- [ ] Code is unusable after its 120-second validity period (REQ-04; TC-12).
- [ ] A late code cannot confirm an expired transfer (REQ-04; TC-12).
- [ ] Repeated confirmation cannot create a second debit (**GAP-03**; analyst decision and test needed).



## 5. Three defect reports

1) Transfers: 567,890 KZT reaches SMS approval despite the 500,000 KZT maximum
2) SMS approval: third wrong code leaves the transfer pending
3) Transfers: daily-limit error shown when both amount and daily limit fail





