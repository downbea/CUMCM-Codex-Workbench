from __future__ import annotations
from collections import defaultdict, deque

def affected_nodes(graph: dict[str,list[str]], changed: list[str]) -> list[str]:
    reverse=defaultdict(list)
    for node,deps in graph.items():
        for dep in deps: reverse[dep].append(node)
    seen=set(changed); q=deque(changed)
    while q:
        cur=q.popleft()
        for nxt in reverse[cur]:
            if nxt not in seen: seen.add(nxt);q.append(nxt)
    return sorted(seen-set(changed))
