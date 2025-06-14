---

## 🧩 Sub-PMD: Document Repository + GPT Integration

### Objective

Build a GPT-based credit research assistant that:

- Loads PDF/text documents into a persistent local vector store
- Enables search + retrieval using LlamaIndex
- Passes query-relevant excerpts to OpenAI's GPT for analysis
- Provides a clean chat interface with history and export capability

### Scope Clarification

- Source documents will be curated and uploaded **only by the project owner** (not end users)
- Uploaded documents will be **persistently stored**, not ephemeral per session
- Streamlit will be used as both frontend and backend framework

---

## 🧱 Features

### Core Functionality

- `data/` folder to hold static source docs (e.g., 10-Ks)
- `ingest.py` to parse + embed those docs to vector DB
- `app.py` to:
  - Provide chat interface
  - Stream responses
  - Maintain full Q&A history
  - Allow export of session history
  - Toggle between default GPT and "Credit Analyst Mode"
- `.env` file to securely store API key and Pinecone/Weaviate config if needed

### Frontend/UI

- Streamlit UI with:
  - Title + instructions
  - Prompt field + submit button
  - Scrollable, auto-height Q&A transcript
  - Button to download transcript (.txt)
  - Dark, readable answer formatting

### Backend Logic

- LlamaIndex for document loading and vector search
- GPT-4 via OpenAI API to answer user prompts
- Persistent `storage/` folder for indexes (excluded from GitHub)
- In-memory session tracking via `st.session_state`
- Support for optional external vector DB (e.g. Pinecone, Weaviate)

---

## 🧪 Test Prompts to Validate MVP

- "Would you lend money to American National Group?"
- "What are their biggest credit risks?"
- "How has their statutory surplus changed year over year?"
- "What is the outlook on their life insurance segment?"
- "Summarize the 2024 risk factors."
- "What do the auditors say about liquidity risk?"
- "How did private loans change between Q4 and Q1?"

---

## 📋 Project Milestones

| Milestone | Description                                                  | Target Date |
| --------- | ------------------------------------------------------------ | ----------- |
| ✅ M1      | Set up project folder and virtual environment                | Day 1       |
| ✅ M2      | Install required packages (`llama-index`, `streamlit`, etc.) | Day 1       |
| ✅ M3      | Add OpenAI API key via `.env`                                | Day 1       |
| ✅ M4      | Write `ingest.py` to process source documents                | Day 1       |
| ✅ M5      | Add real documents (10-K, earnings decks) to `data/`         | Day 1       |
| ✅ M6      | Write `app.py` with Streamlit UI for querying index          | Day 2       |
| ✅ M7      | Confirm model runs locally and answers basic questions       | Day 2       |
| ✅ M8      | Add Q&A history pane + session tracking                      | Day 3       |
| ✅ M9      | Add export/download button for chat history                  | Day 3       |
| ✅ M10     | Push project to GitHub repo                                  | Day 3       |
| ✅ M11     | Deploy to Streamlit Cloud                                    | Day 4       |
| ✅ M12     | Ingest full 10-Q and 10-K into clean Markdown + vector store | Day 4       |
| ☐ M13     | Add Pinecone (Classic) or Weaviate Cloud integration         | Planned     |
| ☐ M14     | Enable cross-device vector loading via cloud backend         | Planned     |

---

## 🧠 Future Enhancements

- Generate draft credit memos from input queries ("Summarize XYZ’s credit profile")
- Display source citations or page references
- Add ability to filter by company, year, document type
- Optional: add user upload capability (later phase)
- Optional: support multi-document and multi-company comparison
- ✅ Toggle between default GPT and Credit Analyst Mode
- ✅ Apply formatting fixes to avoid Markdown glitches
- ✅ Use HTML-based rendering for answers with auto-sizing
- ✅ Use `parse_sec_html.py` to convert raw SEC HTML to clean `.md`
- ✅ Exclude `/storage/` from GitHub repo due to 100MB+ file size
- 🔜 Explore Rule-Aware RAG with Agent Extensions (e.g., Cursor or LangGraph style)

---

## 🗂 Folder Structure

```
credit-analyst-ai/
├── data/               # Controlled PDF/MD inputs
├── storage/            # Persistent vector DB (local only, gitignored)
├── app.py              # Streamlit app
├── ingest.py           # Embeds source docs
├── parse_sec_html.py   # Converts SEC HTML filings to .md
├── .env                # API key and Pinecone config (local only)
├── requirements.txt    # Dependency list
├── README.md           # Setup guide
└── PMD-credit-analyst-ai.md
```

---

## 👤 Project Owner

Todd Nelson

---

## 🔁 Revision History

| Date       | Change Summary                                                                 |
| ---------- | ------------------------------------------------------------------------------ |
| 2025-06-13 | Initial version of PMD for MVP launch                                          |
| 2025-06-13 | Added chat history, export, and clarified upload model                         |
| 2025-06-13 | Added toggle for Analyst Mode, text formatting fixes, and ingestion pipeline   |
| 2025-06-13 | Table rule-aware RAG for future; plan Weaviate integration for cloud-based ops |

