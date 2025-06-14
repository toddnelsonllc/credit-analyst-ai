import os
import re
from bs4 import BeautifulSoup

# === SETTINGS ===
INPUT_FILES = {
    "data/angpa-20250331.html": "data/anginc_10Q_20250331_clean.md",
    "data/angpa-20241231.html": "data/anginc_10K_20241231_clean.md"
}

ITEMS_TO_EXTRACT = [
    "Item 1A",  # Risk Factors
    "Item 2",   # MD&A (10-Q)
    "Item 7",   # MD&A (10-K)
    "Item 8"    # Financial Statements
]

# === HELPERS ===

def extract_items_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'\xa0', ' ', text)

    sections = {}
    for i, item in enumerate(ITEMS_TO_EXTRACT):
        pattern = re.compile(rf"{item.upper()}[\s\S]*?(?=(ITEM [1-9A-Z]{{1,2}}[^A-Za-z]|$))", re.IGNORECASE)
        match = pattern.search(text)
        if match:
            cleaned = match.group(0).strip()
            sections[item] = cleaned
    return sections

# === MAIN ===

for input_path, output_path in INPUT_FILES.items():
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        continue

    with open(input_path, "r", encoding="utf-8") as f:
        html = f.read()

    extracted = extract_items_from_html(html)
    if not extracted:
        print(f"⚠️ No sections found in {input_path}")
        continue

    with open(output_path, "w", encoding="utf-8") as f:
        for item, content in extracted.items():
            f.write(f"# {item}\n\n{content}\n\n")

    print(f"✅ Extracted and saved: {output_path}")
