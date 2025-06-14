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
- `.env` file to securely store API key

### Frontend/UI

- Streamlit UI with:
  - Title + instructions
  - Prompt field + submit button
  - Scrollable Q&A transcript
  - Button to download transcript (JSON or .txt)

### Backend Logic

- LlamaIndex for document loading and vector search
- GPT-4 via OpenAI API to answer user prompts
- Persistent `storage/` folder for indexes (no re-embedding required)
- In-memory session tracking via `st.session_state`

---

## 🧪 Test Prompts to Validate MVP

- "Would you lend money to American National Group?"
- "What are their biggest credit risks?"
- "How has their statutory surplus changed year over year?"
- "What is the outlook on their life insurance segment?"
- "Summarize the 2024 risk factors."
- "What do the auditors say about liquidity risk?"

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
| ☐ M8      | Add Q&A history pane + session tracking                      | Day 3       |
| ☐ M9      | Add export/download button for chat history                  | Day 3       |
| ☐ M10     | Push project to GitHub repo                                  | Day 3       |
| ☐ M11     | Deploy to Streamlit Cloud                                    | Day 4       |
| ☐ M12     | Share link with trusted users for feedback                   | Day 4       |

---

## 🧠 Future Enhancements

- Generate draft credit memos from input queries ("Summarize XYZ’s credit profile")
- Display source citations or page references
- Add ability to filter by company, year, document type
- Optional: add user upload capability (later phase)
- Optional: support multi-document and multi-company comparison

---

## 🗂 Folder Structure

```
credit-analyst-ai/
├── data/               # Controlled PDF inputs
├── storage/            # Persistent vector DB
├── app.py              # Streamlit app
├── ingest.py           # Embeds source docs
├── .env                # API key (local only)
├── requirements.txt    # Dependency list
├── README.md           # Setup guide
└── PMD-credit-analyst-ai.md
```

---

## 👤 Project Owner

Todd Nelson

---

## 🔁 Revision History

| Date       | Change Summary                                         |
| ---------- | ------------------------------------------------------ |
| 2025-06-13 | Initial version of PMD for MVP launch                  |
| 2025-06-13 | Added chat history, export, and clarified upload model |

