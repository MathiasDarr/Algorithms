"""
LeetCode

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
circles among all the students.


DISJOINT SET UNION
A disjoint set union DSU data structure can be used to maintain knowledge of the connected components of a graph, and query
for them quickly.


DFS Solution:





Union Find Solution:

    Iterate through the matrix of friend connections,
        - For each connection, perform a union s.t that the value in the parent array for both of these values is the same

    - Now iterate through the parent array of the DSU object
        - Add the unique values to a set
            - make use of find





 """

class DSU:
    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:

    def findCircleNum(self, M):

        def dfs(node):
            for i, friendship in enumerate(M[node]):
                if friendship and i not in seen:
                    seen.add(i)
                    dfs(i)

        N = len(M)
        seen = set()
        count = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                count +=1

        return count


    # def findCircleNum(self, M):
    #     N = len(M)
    #     dsu = DSU(N)
    #
    #     for i in range(N):
    #         for j in range(i):
    #             if M[i][j] == 1:
    #                 dsu.union(i,j)
    #     s = set()
    #     for p in dsu.parent:
    #         s.add(dsu.find(p))
    #     return len(s)



M = [[1,1,0],
 [1,1,1],
 [0,1,1]]

solution = Solution()

solution.findCircleNum(M)
