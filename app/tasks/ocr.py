from app.tasks.base import Task


def _resolver(query: str) -> str:
    # Simulated OCR extraction from an image
    return "Price: $19.99\nItem: Wireless Mouse\nQuantity: 2\nTotal: $39.98"


task = Task(
    name="OCR",
    description=(
        "Optical Character Recognition for images and scanned documents. Returns extracted "
        "text along with confidence metadata when available. Input: images or image URLs; "
        "Output: raw extracted text and structured fields for tables/forms. Edge cases: low-"
        "quality images, handwriting, mixed languages - resolver should attempt language "
        "detection and fallback gracefully."
    ),
    resolver=_resolver,
)
