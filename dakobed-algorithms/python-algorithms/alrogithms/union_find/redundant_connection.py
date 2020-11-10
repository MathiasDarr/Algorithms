"""
 In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge
that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers,
return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format,
with u < v.

Tree:
Every node must be connected to every other node through a single path ( NO CYCLES)

Given input is a graph that started as a tree w/ N nodes w/ distint values 1,2 ... N w/ one addiontal edge added.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.



UNION FIND SOLUTION:

A disjoint set union DSU data structure can be used to maintain knowledge of the connect components of a graph, and query
for them quickly.
    - find -> outputs unique id s.t two nodes ahve the same ID if and only if the yare in the same connected component
    - union -> Forms an edge (x,y) in the graph, connecting the components w/ find(x) & find(y) together

We are searching for an edge the forms a cycle w/in the graph

All nodes initially belong to their own components

Traverse the edges
    -  As we trraverse the edges, nodes connected by an edge are added to the same component
    -  If we encounter two nodes that are in the same componenet, this means that a cycle has been detected & this edge
        is to be removed.

DFS SOLUTION:




"""

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if self.find(x) == self.find(y):
            return False

        self.parent[self.find(x)] = self.find(y)
        return True

from collections import defaultdict
class Solution:

    def findRedundantConnectionDFS(self, edges):
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(neighbor, target) for neighbor in graph[source])

        graph = defaultdict(set)
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFind(n + 1)


        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge



solution = Solution()
edges = [[1,2], [1,3], [2,3]]

solution.findRedundantConnection(edges)