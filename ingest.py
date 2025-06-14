import os
from dotenv import load_dotenv

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Confirm it worked
if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file.")

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Build the vector index
index = VectorStoreIndex.from_documents(documents)

# Save the index to disk
index.storage_context.persist(persist_dir="storage")

print("✅ Document index built and saved successfully.")
