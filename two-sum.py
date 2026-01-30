"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# brute force
# point/select each element, starting from the beginning, then add the value right of the value
# after adding each time, compare with target to see if it makes up that target value.
# if it does make up that target value, return those two indices.
def returnIndicesThatSumUpToTarget (nums, target):
    n = len(nums) # e.g. len(nums[3,6,9]) returns 3.
    # iterate from 0, starting index, to the last index n
    for i in range(n):
        # as we are selecting the value, we need to also select values right next to values with i index
        for j in range(i + 1, n):
            if sum(nums[i], nums[j]) == target:
                return [i,j]
    return False

# optimal solution
def returnIndicesThatSumUpToTarget (nums, target):
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in nums:
            return [i,nums[complement]]


