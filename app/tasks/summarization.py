from app.tasks.base import Task


def _resolver(query: str) -> str:
    return "Here is a concise summary of the provided text: duh."


task = Task(
    name="Summarization",
    description=(
        "Produce concise, accurate summaries of input text tailored to the requested length "
        "and style. Supports extractive and abstractive summarization modes. Input: single "
        "documents or multiple passages. Output: a short summary; optionally bullet points "
        "or TL;DR. Edge cases: preserving critical facts, handling contradictory inputs, "
        "and maintaining neutral tone when required."
    ),
    resolver=_resolver,
)
