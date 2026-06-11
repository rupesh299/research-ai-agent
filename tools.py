from duckduckgo_search import DDGS

def search_web(query):
    results = DDGS().text(query, max_results=5)

    output = []

    for r in results:
        output.append(
            f"Title: {r['title']}\n"
            f"URL: {r['href']}\n"
            f"Snippet: {r['body']}\n"
        )

    return "\n".join(output)