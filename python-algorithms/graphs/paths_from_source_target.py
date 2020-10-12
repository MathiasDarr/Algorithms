class Solution:
    def allPathsSourceTarget(self, graph):
        N = len(graph)
        paths = []
        def backtrack(candidate):
            if candidate[-1] == N-1:
                paths.append(candidate.copy())
                return
            for choice in graph[candidate[-1]]:
                candidate.append(choice)
                backtrack(candidate)
                candidate.pop()
        backtrack([0])
        return paths

    def allpaths(self, graph):
        N = len(graph)
        paths = []
        def dfs(path):
            if path[-1] == N-1:
                paths.append(path)
                return
            for node in graph[path[-1]]:
                dfs(path+[node])
        dfs([0])
        return paths
graph = [[1,2],[3],[3],[]]

solution = Solution()
solution.allpaths(graph)