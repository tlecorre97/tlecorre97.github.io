from scholarly import scholarly
import json

author_id = "vLpZJu0AAAAJ"
author = scholarly.search_author_id(author_id)
author = scholarly.fill(author, sections=["publications"])

publications = []
for pub in author["publications"]:
    filled = scholarly.fill(pub)
    bib = filled.get("bib", {})
    publications.append({
        "title": bib.get("title", "Sans titre"),
        "year": bib.get("pub_year", "N/A"),
        "venue": bib.get("venue", ""),
        "url": filled.get("pub_url", "#"),
    })

with open("publications.json", "w", encoding="utf-8") as f:
    json.dump(publications, f, indent=2, ensure_ascii=False)
