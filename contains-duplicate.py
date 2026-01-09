# problem statement
"""
Problem: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1]
Output: false
"""

# brute force solution
def isDup(nums: list[int]) -> bool:
    n = len(nums)
    for i in range(n): # runs n times 
        for j in range(i + 1, n): # for each fixed i, 
            # inner loop runs from (j = i + 1 to n - 1) 
            # which is n - i - 1 comparisons
            if nums[i] == nums[j]:
                return True
    return False
# the time complexity is O(n^2).
# Why? See the comments in-line with code

# optimal solution
def isDup(nums: list[int]) -> bool:
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False
# range(start, end-1) and len(datastructure) returns an int value that is the size of the data structure

"""
Your algorithm does n iterations.

Each iteration does constant expected work because set lookup/insert are constant expected time.

Therefore total expected time is O(n).
"""