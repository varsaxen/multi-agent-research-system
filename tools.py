"""
Mock tools (no internet needed)
"""

from langchain.tools import tool

@tool
def web_search(query: str):
    """Search the web for a given query and return relevant content."""

    try:
        print(f"[TOOL] web_search -> {query}")

        return [
            {
                "url": "https://example.com/1",
                "content": "AI in banking improves efficiency."
            },
            {
                "url": "https://example.com/2",
                "content": "AI reduces fraud detection time."
            }
        ]

    except Exception as e:
        return [{"error": str(e)}]


@tool
def scrape_url(url: str):
    """Extract and clean text content from a URL."""

    return f"Cleaned content from {url}"


@tool
def assess_source(content: str):
    """Evaluate credibility of source content and return score between 0–10."""

    return {"score": 8}