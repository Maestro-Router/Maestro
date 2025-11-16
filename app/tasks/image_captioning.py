from app.tasks.base import Task


def _resolver(query: str) -> str:
    return "A beautiful sunrise over a mountain range with a clear sky."


task = Task(
    name="Image Captioning",
    description=(
        "Generate descriptive, context-aware captions for images. Useful for accessibility, "
        "content moderation, and metadata generation. Input: single image or multiple views; "
        "Output: a short descriptive caption, optionally with objects detected and scene "
        "context. Edge cases: ambiguous scenes, sensitive content; resolver should signal "
        "uncertainty when appropriate."
    ),
    resolver=_resolver,
)
