#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx


def dfs_edges(G, source=None):
    if source is None:
        nodes = G
    else:
        nodes = [source]
    visited = set()
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, len(G), iter(G[start]))]
        while stack:
            (parent, depth_now, children) = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    yield (parent, child)
                    visited.add(child)
                    if depth_now > 1:
                        stack.append((child, depth_now - 1,
                                iter(G[child])))
            except StopIteration:
                stack.pop()


G = nx.gnm_random_graph(10, 15, directed=True)
print list(dfs_edges(G, source=0))
nx.draw_networkx(G)

			
