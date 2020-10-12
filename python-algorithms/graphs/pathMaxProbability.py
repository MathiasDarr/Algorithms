from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):

        adjacenyList = defaultdict(list)
        for i, (node1, node2) in enumerate(edges):
            adjacenyList[node1].append((node2, succProb[i]))
            adjacenyList[node2].append((node1, succProb[i]))

        probs = {i: 0 for i in range(n)}
        probs[start] = 1
        seen = {start}
        queue = [(-1, start)]

        while queue:
            prob, node = heapq.heappop(queue)
            seen.add(node)
            for adjNode, adjProb in adjacenyList[node]:
                if adjNode not in seen:
                    newProb = adjProb * prob
                    if newProb < probs[adjNode]:
                        probs[adjNode] = newProb
                        heapq.heappush(queue, (newProb, adjNode))

        return -probs[end]
n = 5
edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
start = 3
end = 4

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.2]
# start = 0
# end = 2

solution = Solution()
solution.maxProbability(n, edges, succProb, start, end)


#     seen = {start}
#     queue = [start]
#     while len(queue) > 0:
#         node = queue.pop(0)
#         seen.add(node)
#         adjacentNodes = adjacenyList[node]
#         sortedNodes = sorted(adjacentNodes, key=lambda x: x[1], reverse=True)
#         for i in range(len(sortedNodes)):
#             adjNode = sortedNodes[i][0]
#             adjProb = sortedNodes[i][1]
#             if adjNode not in seen:
#                 queue.append((adjNode, adjProb))
#
#         if distances[node] >  distances[node]
#
#
#         # maxProb = 0
#         # mostProbableAdjacentNode = None
#         #
#         # for adjnode, prob in adjacentNodes:
#         #     if prob > maxProb:
#         #         maxProb = prob
#         #         mostProbableAdjacentNode = adjnode
#
#         #
#         # for adjnode, prob in adjacenyList[node]:
#         #     maxProb = 0
#         #     mostProbableAdjacentNode = None
#         #     if adjnode not in seen:
#         #         if prob > maxProb:
#         #             maxProb = max(maxProb, prob)
#         #             mostProbableAdjacentNode = adjnode
#         #     queue
#
# # def maxProbability(self, n: int, edges, succProb, start, end):
# #     queue = [(start, 1, {start})]
# #     hashMap = defaultdict(list)
# #     maxProba = 0
# #     for i, edge in enumerate(edges):
# #         node1 = edge[0]
# #         node2 = edge[1]
# #         hashMap[node1].append((node2, succProb[i]))
# #         hashMap[node2].append((node1, succProb[i]))
# #
# #     while len(queue):
# #         node, probability, visited = queue.pop(0)
# #         if node == end:
# #             maxProba = max(maxProba, probability)
# #         else:
# #             for adjacentNode, p in hashMap[node]:
# #                 if adjacentNode not in visited:
# #                     queue.append((adjacentNode, probability * p, {*visited, adjacentNode}))
# #     return maxProba