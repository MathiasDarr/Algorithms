"""There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
circles among all the students. """


from collections import deque

class Solution:
    def findCircleNum(self, M):

        count = 0
        queue = deque()
        N = len(M)

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    count +=1
                    M[i][j] = 0
                    queue.append(j)
                    while queue:
                        tmp = queue.popleft()
                        for t in range(N):
                            if M[tmp][t] == 1:
                                queue.append(t)
                                M[tmp][t] = 0

        return count


M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

solution = Solution()

solution.findCircleNum(M)
