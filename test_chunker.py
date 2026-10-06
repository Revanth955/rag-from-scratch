from rag.chunker import chunk_text

with open("data/company_policy.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text, chunk_size=100, overlap=20)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i} ---")
    print(chunk)
