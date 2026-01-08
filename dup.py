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

