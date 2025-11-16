from app.tasks.base import Task


def _resolver(query: str) -> str:
    return "Here is the generated image based on your description."


task = Task(
    name="Image Generation",
    description=(
        "Create new images from textual descriptions. Supports style, aspect ratio, and "
        "basic scene composition directives. Input: a descriptive prompt describing desired "
        "content and style; Output: link or binary image data plus metadata about style "
        "and seed. Edge cases: content safety, trademarked characters, and highly "
        "detailed requests that may require multiple passes."
    ),
    resolver=_resolver,
)
