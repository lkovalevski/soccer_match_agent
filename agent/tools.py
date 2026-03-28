import requests
from bs4 import BeautifulSoup
from framework.game_framework import register_tool
from litellm import completion


@register_tool(tags=["news"])
def fetch_article(url: str) -> str:
    """
    Fetches and extracts clean text from a news article URL.
    Returns only the article body text, ready for analysis.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    for tag in soup(["script", "style", "nav", "header", "footer",
                     "aside", "form", "iframe", "noscript"]):
        tag.decompose()
    
    # Buscar el contenido principal del artículo
    article = (
        soup.find("article") or
        soup.find(class_=lambda c: c and "post-content" in str(c)) or
        soup.find(class_=lambda c: c and "entry-content" in str(c)) or
        soup.find("main") or
        soup.find("body")
    )
    
    text = article.get_text(separator="\n") if article else soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean = "\n".join(lines)
    
    return clean[:3000]  # texto limpio, listo para analizar


@register_tool(tags=["analysis"])
def summarize_match_outlook(text: str) -> str:
    """
    Produces a structured analysis of Newell's upcoming match
    based on the provided article text.
    """

    prompt = f"""
You are a professional football analyst.

Based on the following article, produce a structured pre-match analysis
focused on Newell's Old Boys' upcoming match.

Structure your answer as:

1. Current Team Situation
2. Strengths
3. Weaknesses
4. Tactical Outlook
5. Psychological Context
6. Expected Match Scenario

Article:
{text}
"""

    response = completion(
        model="openai/gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )

    return response.choices[0].message.content


@register_tool(tags=["system"], terminal=True)
def terminate(message: str) -> str:
    """
    Terminates the agent execution with a final analysis.
    """
    return message
