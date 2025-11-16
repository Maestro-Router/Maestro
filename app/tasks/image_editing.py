from app.tasks.base import Task


def _resolver(query: str) -> str:
    return "This image now looks perfect!"

task = Task(
    name="Image Editing",
    description=(
        "Edit or retouch images according to user instructions, such as object removal, "
        "color adjustments, or compositing elements. Input: original image + edit instructions; "
        "Output: edited image data and a short log of applied edits. Edge cases: high-"
        "precision edits, licensing, and preserving original image metadata when required."
    ),
    resolver=_resolver,
)
