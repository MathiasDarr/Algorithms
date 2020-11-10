class Solution:
    def partitionLabels(self, S):
        pass

solution = Solution()
S = "ababcbacadefegdehijhklij"




from collections import defaultdict

def processLogs(logs, threshold):
    transactions_count = defaultdict(int)

    output = []

    for log in logs:
        print(1)
        line = log.split(" ")
        suid = line[0]
        transactions_count[suid] += 1
        if transactions_count[suid] == threshold:
            output.append(suid)
    return sorted(output)


def numberOfItems(s, startIndices, endIndices):
    output = []
    containers_map = defaultdict(int)
    left = - 1
    count = 0
    for index, c in enumerate(s):
        if c == '|':
            if left >= 0:
                containers_map[(left, index)] = count
            left = index
            count = 0
        elif c == '*':
            count += 1

    for start, end in zip(startIndices, endIndices):
        print("The interval {} -  {}".format(start,end))
        items = 0
        for start_container, end_container in containers_map.keys():
            print("The start of the container: {}-{}".format(start_container, end_container))

            if start_container >= start-1 and end_container <= end-1:
                items += containers_map[(start_container, end_container)]
            print("The number of items is: {}".format(items))
        output.append(items)
    return output


s = '|**|*|*|'
start = [1,1]
end = [5,6]
numberOfItems(s, start, end)



