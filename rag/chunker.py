import re


def chunk_text(text, chunk_size=200, overlap=50):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_sentences = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence)

        if current_length + sentence_length > chunk_size and current_sentences:
            chunks.append(" ".join(current_sentences))

            # Keep the last sentence as overlap
            overlap_sentences = []
            overlap_length = 0

            for s in reversed(current_sentences):
                if overlap_length + len(s) > overlap:
                    break

                overlap_sentences.insert(0, s)
                overlap_length += len(s)

            current_sentences = overlap_sentences
            current_length = overlap_length

        current_sentences.append(sentence)
        current_length += sentence_length + 1

    if current_sentences:
        chunks.append(" ".join(current_sentences))

    return chunks