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

# Mode selector
mode = st.radio("Choose AI Mode:", ["🔓 Default GPT", "🧠 Credit Analyst Mode"])

# Reasoning instruction
analyst_prompt = (
    "You are a senior credit analyst. When answering questions, do the following:\n"
    "1. Identify quarter-over-quarter changes in loan exposures or credit quality.\n"
    "2. Flag increases in BB or below holdings.\n"
    "3. Quantify material shifts in private loans or high-yield categories.\n"
    "4. Use specific numbers, percentages, and trend direction.\n"
    "5. Avoid generic language. Always tie response to actual data when possible.\n"
)

# Input box (multiline and resizable)
query = st.text_area(
    "💬 Enter your question below:",
    height=100,
    placeholder="e.g. What are the major credit risks?",
)

# Process response
if st.button("Submit") and query.strip():
    with st.spinner("Analyzing..."):
        if mode == "🧠 Credit Analyst Mode":
            final_prompt = f"{analyst_prompt}\n\nUser: {query.strip()}"
        else:
            final_prompt = query.strip()

        response = query_engine.query(final_prompt)
        answer = response.response
        st.session_state.chat_history.append({"query": query, "response": answer})

# Show chat history
if st.session_state.chat_history:
    st.markdown("### 🧠 Conversation History")

    for i, pair in enumerate(st.session_state.chat_history, 1):
        st.markdown(f"**Q{i}:** {pair['query']}")

        # Format the response into HTML with dark font and line breaks
        st.markdown(
            f"<div style='color:#111111; font-size:16px; font-family:Arial, sans-serif; "
            f"background-color:#f8f9fa; padding:10px; border-radius:5px; border:1px solid #ddd;'>"
            f"{pair['response'].replace(chr(10), '<br>')}"
            f"</div>",
            unsafe_allow_html=True
        )

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
