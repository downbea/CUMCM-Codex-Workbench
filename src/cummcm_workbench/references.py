from __future__ import annotations

def format_gbt7714(item: dict, index: int) -> str:
    authors=item.get('authors') or item.get('author') or '作者待核验'
    if isinstance(authors,list): authors=', '.join(authors)
    title=item.get('title','题名待核验'); year=item.get('year','年份待核验')
    kind=item.get('type','journal')
    if kind=='book': return f'[{index}] {authors}. {title}[M]. {item.get("place","出版地待核验")}: {item.get("publisher","出版社待核验")}, {year}.'
    if kind=='web': return f'[{index}] {authors}. {title}[EB/OL]. {item.get("url","链接待核验")}, {item.get("accessed","访问日期待核验")}.'
    return f'[{index}] {authors}. {title}[J]. {item.get("journal","期刊待核验")}, {year}, {item.get("volume","卷待核验")}({item.get("issue","期待核验")}): {item.get("pages","页码待核验")}.'
