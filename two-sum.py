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
    # Example: nums = [2,7,11,15], target = 17
    seen = {}
    for index, element in enumerate(nums): 
    # 1. we iterate over the indices and values of num. This is an easy way to call out the values of "index" and "element"
        complement = target - element 
        # 2. for each element, compute complement so complement = 17 - 2 = 15
        # 5. complement = 17 - 7 = 10
        # 8. complement = 17 - 11 = 6
        # 11. complement = 17 - 15 = 2
        if complement in seen: 
        # 3. first iteration, nothing there; complement is not in seen. # note: it is ok to not have anything because you need two elements that add up to target, not 1.
        # 6. 10 is not in seen    
        # 9. 6 is not in seen
        # 12. 2 is in seen
            return [index, seen[complement]]
            # 13. return the index that we are at which is 3, aka 4th number. and seen[complement] is seen[2] = 0 from step 10 e.i {2:0, 7:1, 11:3} # returns "[3,0]"
        seen[element] = index 
        # 4. seen[element] is 2 and its assignment is 0 e.i. {2:0}
        # 7. seen[element] is 7 and its assignment is 1 e.i. {2:0, 7:1}
        # 10. seen[element] is 11 and its assignment is 3 e.i {2:0, 7:1, 11:3}  
    return None

