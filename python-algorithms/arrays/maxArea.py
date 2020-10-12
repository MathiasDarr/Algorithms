


def maxArea(height):
    left = 0
    right = len(height) - 1
    maxarea = float('-inf')

    while left < right:
        area = (right-left)*min(height[left], height[right])
        if area > maxarea:
            maxarea = area
        if height[left] < height[right]:
            left +=1
        else:
            right -= 1

    return maxarea

nums = [1,8,6,2,5,4,8,3,7]
maxarea = maxArea(nums)