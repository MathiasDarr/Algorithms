"""
[i,j] to take course i, you first have to take course j

Given a list of prerequisite pairs, is it possible to finish all courses



"""

from collections import defaultdict
import enum
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # adjList = defaultdict(list)
        # indegree = [0] * numCourses
        #
        # for pre in prerequisites:
        #     adjList[pre[1]].append(pre[0])
        #     indegree[pre[0]] +=1
        # q = []
        #
        # for i, value in enumerate(indegree):
        #     if value ==0:
        #         q.append(i)
        # count = 0
        # while len(q) > 0:
        #     cur = q.pop()
        #     if indegree[cur] ==0:
        #         count +=1
        #     if cur not in adjList:
        #         continue
        #     for neighbor in adjList.get(cur):
        #         indegree[neighbor] -=1
        #         if indegree[neighbor] ==0:
        #             q.append((neighbor))
        # return count ==numCourses

    def canFinish(self, numCourses, prerequisites):
        if numCourses == 0:
            return False
        adjlist = defaultdict(list)
        for course, pre in prerequisites:
            adjlist[course].append(pre)
        state = {i:0 for i in range(numCourses)}

        # state == 0 unprocessed
        # state == -1 processing
        # state = 1 visited
        def isCyclic(courseID):
            if state[courseID] == 1:
                return False
            if state[courseID] == -1:
                return True
            # Set state to -1
            state[courseID] = -1
            for v in adjlist[courseID]:
                if isCyclic(v):
                    return True
            state[courseID] = 1
            return False

        for u in range(numCourses):
            if isCyclic(u):
                return False

        return True


numCourses = 2
prerequisites = [[1,0], [0,1]]

solution = Solution()
solution.canFinish(numCourses, prerequisites)