import streamlit as st
from dotenv import load_dotenv
import os
from llama_index.core import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.query_engine import RetrieverQueryEngine

# ✅ Must be first Streamlit call
st.set_page_config(page_title="Credit Analyst AI", layout="centered")

# System instruction prompt for formatting and tone
instruction = (
    "You are a credit research analyst. "
    "When answering questions that involve quarter-over-quarter comparisons or any numeric change, "
    "round all percentage figures to one decimal place (e.g., 7.2% not 7.24%). "
    "Keep responses clear, professional, and concise."
)

# Load API key
load_dotenv()

# Load index
@st.cache_resource
def load_index():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    return load_index_from_storage(storage_context)

index = load_index()
query_engine = RetrieverQueryEngine.from_args(index.as_retriever())

# App header
st.title("📊 Credit Analyst AI")
st.caption("Ask questions about a company’s credit profile.")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box (multiline and resizable)
query = st.text_area(
    "💬 Enter your question below:",
    height=100,
    placeholder="e.g. What are the major credit risks?",
)

# Submit button
if st.button("Submit") and query.strip():
    with st.spinner("Analyzing..."):
        final_prompt = f"{instruction}\n\nUser: {query.strip()}"
        response = query_engine.query(final_prompt)
        answer = response.response
        st.session_state.chat_history.append({"query": query, "response": answer})

# Show chat history
if st.session_state.chat_history:
    st.markdown("### 🧠 Conversation History")
    for i, pair in enumerate(st.session_state.chat_history, 1):
        st.markdown(f"**Q{i}:** {pair['query']}")
        st.markdown(f"**A{i}:** {pair['response']}")
        st.markdown("---")

    # Exportable transcript text
    full_text = ""
    for pair in st.session_state.chat_history:
        full_text += f"Q: {pair['query']}\nA: {pair['response']}\n\n"

    st.download_button(
        label="📥 Download Chat History (.txt)",
        data=full_text,
        file_name="credit_analyst_chat.txt",
        mime="text/plain"
    )

# Reset chat button
if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()
