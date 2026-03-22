from __future__ import annotations

from math import sqrt


def parse_signature(signature: str) -> list[float]:
    if not signature:
        return []
    try:
        return [float(value) for value in signature.split(",") if value]
    except ValueError as exc:
        raise ValueError("Invalid histogram signature.") from exc


def compare_image_similarity(query_signature: str, stored_signature: str) -> float:
    """
    Histogram similarity reference implementation using cosine similarity.
    Returns a value in [0.0, 1.0].
    """
    vector_a = parse_signature(query_signature)
    vector_b = parse_signature(stored_signature)

    if not vector_a or not vector_b or len(vector_a) != len(vector_b):
        raise ValueError("Histogram signatures are missing or incompatible.")

    dot = sum(a * b for a, b in zip(vector_a, vector_b))
    norm_a = sqrt(sum(a * a for a in vector_a))
    norm_b = sqrt(sum(b * b for b in vector_b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)
