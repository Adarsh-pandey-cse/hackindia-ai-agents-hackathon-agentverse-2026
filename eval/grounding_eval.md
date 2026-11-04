# Grounding Evaluation Report

This evaluation assesses the grounded document question-answering system on benchmark test queries spanning document-backed factual queries and out-of-domain unanswerable queries.

## Evaluation Methodology
1. **Evidence Retrieval:** Top candidate chunks retrieved using vector/lexical matching from `data/chunks.json`.
2. **Citation Integrity Check:** Regular expression parser extracts all `[source: <chunk_id>, page: <page>]` tags from the generated text and verifies they match the retrieved chunk IDs.
3. **Grounding Verification:** Answer assertions must be explicitly supported by the cited chunk without external extrapolation.
4. **Refusal Benchmark:** Questions lacking sufficient evidence in the source documents must trigger a strict refusal: *"I could not find this in the provided documents."*

## Test Evaluation Results

| ID | Test Question | Retrieved Chunks | Generated Answer with Citation | Citation Status | Grounding Status | Notes |
|:---|:---|:---|:---|:---:|:---:|:---|
| **Q1** | What is the refund window for receiving a full 100% tuition refund? | `refund_policy_p1_c1` | 100% Refund Window: A full 100% refund of tuition and academic fees (minus a nominal administrative processing fee) will be granted if formal withdrawal noti... | Valid | PASS | Supported by chunk refund_policy_p1_c1. |
| **Q2** | Who can apply for the hostel Wi-Fi pass and how many devices are allowed? | `college_faq_p2_c1` | Wi-Fi Pass Eligibility: All registered hostel residents and enrolled day scholars are eligible to apply for an active high-speed campus Wi-Fi pass via the St... | Valid | PASS | Supported by chunk college_faq_p2_c1. |
| **Q3** | Can I pay semester fees using UPI, and what happens if I pay late after 15 August? | `college_faq_p4_c1` | Payment Channels: Students can pay semester tuition fees, hostel rent, and examination dues electronically via UPI, net banking, or debit/credit cards throug... | Valid | PASS | Supported by chunk college_faq_p4_c1. |
| **Q4** | What administrative processing fee is deducted from approved refund requests? | `refund_policy_p2_c1` | Administrative Processing Deduction: For all eligible refund claims processed within the 100% refund window, an administrative processing fee deduction of Rs... | Valid | PASS | Supported by chunk refund_policy_p2_c1. |
| **Q5** | What is the overdue fine for returning library books late? | `college_faq_p3_c1` | Overdue Penalties: Borrowers who fail to return or renew books by the due date are subject to an overdue late return fine of Rs 10 per day per book for the f... | Valid | PASS | Supported by chunk college_faq_p3_c1. |
| **Q6** | Are students permitted to park personal electric scooters inside hostel bedrooms? | `none` | I could not find this in the provided documents. | N/A (Refusal) | PASS | Strict refusal honored. Zero hallucinated citations. |

## Summary Metrics
- **Total Test Cases:** 6
- **Grounded Answers:** 6 / 6 (100.0%)
- **Valid Citations Extracted:** 12
- **Broken Citations Detected:** 0
- **Refusal Accuracy:** 1 / 1 (100.0%)
- **Overall Status:** ALL CHECKS PASSED

## Failure & Edge Case Handling
- **Broken Citation Prevention:** If the model hallucinates a non-retrieved chunk ID (e.g. `hostel_rules_p9_c4`), the citation verification validator immediately flags it as broken and strips unverified assertions.
- **Out-of-Scope Queries:** When the retrieval score falls below the confidence cutoff (0.22), the system declines to generate speculative answers, safeguarding enterprise reliability.
