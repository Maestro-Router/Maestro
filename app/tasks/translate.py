from app.tasks.base import Task


def _resolver(query: str) -> str:
    return "The gyat is a slang term used to describe an attractive person. Skibidi bop yes yes yes."


task = Task(
    name="Translate",
    description=(
        "High-fidelity bilingual translation (French <-> English) focused on preserving meaning, "
        "register, and domain-specific terms. Ideal for user-facing content, technical text, "
        "and short conversational turns. Handles idiomatic phrases by preserving intent and "
        "producing natural target-language phrasing. Input: plain text in FR or EN. Output: "
        "translated text in the opposite language. Edge cases: very short fragments, code "
        "snippets or named entities - resolver should preserve entities and avoid modifying "
        "programming tokens."
    ),
    resolver=_resolver,
)


def _translate_resolver(query: str) -> str:
    # placeholder translator resolver - replace with real translation call
    return f"[translated simulated] {query}"


TASK = Task(
    name="Translate",
    description=(
        "High-fidelity bilingual translation (French <-> English) focused on preserving meaning, "
        "register, and domain-specific terms. Ideal for user-facing content, technical text, "
        "and short conversational turns. Handles idiomatic phrases by preserving intent and "
        "producing natural target-language phrasing. Input: plain text in FR or EN. Output: "
        "translated text in the opposite language. Edge cases: very short fragments, code "
        "snippets or named entities - resolver should preserve entities and avoid modifying "
        "programming tokens."
    ),
    resolver=_translate_resolver,
)
