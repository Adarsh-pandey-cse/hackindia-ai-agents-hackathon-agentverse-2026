# Grounded Document QA - Example Queries and Cited Answers

This document catalogs representative question-answering interactions demonstrating grounded retrieval, verbatim citations, and boundary refusal on unanswerable queries.

---

### Example 1: Refund Window Policy
- **Question:** What is the refund window for receiving a full 100% tuition refund?
- **Retrieved Chunk ID:** `refund_policy_p1_c1`
- **Source Document:** `refund_policy.txt` (Page 1)
- **Answer:**
  > A full 100% refund of tuition and academic fees (minus a nominal administrative processing fee) will be granted if formal withdrawal notice is received in writing within 7 days of initial fee payment or at least 15 days before commencement of classes [source: refund_policy_p1_c1, page 1].
- **Grounding Verification:** Validated. Citation matches retrieved chunk text.

---

### Example 2: Campus Wi-Fi Pass and Device Quota
- **Question:** Who can apply for the hostel Wi-Fi pass and how many devices are allowed?
- **Retrieved Chunk ID:** `college_faq_p2_c1`
- **Source Document:** `college_faq.txt` (Page 2)
- **Answer:**
  > All registered hostel residents and enrolled day scholars are eligible to apply for an active high-speed campus Wi-Fi pass, and each student is entitled to register a maximum of two personal devices on the secure network [source: college_faq_p2_c1, page 2].
- **Grounding Verification:** Validated. Both claims supported by cited chunk.

---

### Example 3: Fee Payment Options and Late Fine
- **Question:** Can I pay semester fees using UPI, and what happens if I pay late after 15 August?
- **Retrieved Chunk ID:** `college_faq_p4_c1`
- **Source Document:** `college_faq.txt` (Page 4)
- **Answer:**
  > Students can pay semester tuition fees electronically via UPI, net banking, or debit/credit cards through the ERP portal [source: college_faq_p4_c1, page 4]. If payment is completed after the 15 August deadline, a mandatory late fee fine of Rs 500 applies up to 31 August [source: college_faq_p4_c1, page 4].
- **Grounding Verification:** Validated. Facts and monetary amounts strictly grounded.

---

### Example 4: Administrative Cancellation Deduction
- **Question:** What administrative processing fee is deducted from approved refund requests?
- **Retrieved Chunk ID:** `refund_policy_p2_c1`
- **Source Document:** `refund_policy.txt` (Page 2)
- **Answer:**
  > For all eligible refund claims processed within the 100% refund window, an administrative processing fee deduction of Rs 250 is retained [source: refund_policy_p2_c1, page 2].
- **Grounding Verification:** Validated. Exact penalty figure cited correctly.

---

### Example 5: Library Overdue Penalties
- **Question:** What is the overdue fine for returning library books late?
- **Retrieved Chunk ID:** `college_faq_p3_c1`
- **Source Document:** `college_faq.txt` (Page 3)
- **Answer:**
  > Borrowers who fail to return or renew books by the due date are subject to an overdue late return fine of Rs 10 per day per book for the first 7 days of delay, increasing to Rs 20 per day thereafter [source: college_faq_p3_c1, page 3].
- **Grounding Verification:** Validated. Exact tiered fine cited directly.

---

### Example 6: Refusal on Unanswerable Query (Hallucination Prevention)
- **Question:** Are students permitted to park personal electric scooters inside hostel bedrooms?
- **Retrieved Chunks:** Similarity scores below confidence threshold (0.15).
- **Answer:**
  > I could not find this in the provided documents.
- **Grounding Verification:** Validated. The system strictly refused to invent parking regulations or produce broken/unsupported citations.
