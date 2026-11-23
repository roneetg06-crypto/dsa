"""
Problem : Find the Largest Element in an Array
Pattern : Traversal

Approach (apne shabdon mein):
  1. Create a variable for maximum element(maxi).
  2. Iterate the loop and obtain the maximum element.

Time  : O(N)
Space : O(1)
"""


def largest(nums):

    n = len(nums)
    maxi = float('-inf')
    for i in range(0, n):
        if maxi < nums[i]:
            maxi = max(maxi, nums[i])

    return maxi
        


if __name__ == "__main__":
    assert largest([3, 1, 9, 4]) == 9 
    assert largest([5]) == 5
    assert largest([-3, -1, -7]) == -1
    print("All tests passed")