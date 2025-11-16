from app.tasks.base import Task


def _resolver(query: str) -> str:
    urls = [
        "https://stackoverflow.com/questions/12345678/example-question",
        "https://medium.com/@example/example-article-abcdef123456",
        "https://github.com/example/repo/blob/main/README.md"
    ]
    return "Here are some relevant links:\n" + "\n".join(urls)


task = Task(
    name="Web Search",
    description=(
        "Search the web and return a concise set of relevant results and source links. "
        "Designed to extract and surface factual snippets, authoritative references, and "
        "URLs that support user queries. Input: user information request or question. Output: "
        "a ranked list of short snippets with source URLs. Edge cases: ambiguous queries, "
        "requests for personal data or paid content. The resolver should favor high-quality "
        "domains and include snippet context when possible."
    ),
    resolver=_resolver,
)
