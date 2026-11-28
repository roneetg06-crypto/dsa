"""
Problem : Find the linear_search Element in an Array
Pattern : Traversal

Approach (apne shabdon mein):
  1. 
  2.

Time  : O(N)
Space : O(1)
"""


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return - 1


if __name__ == "__main__":
    assert linear_search([3, 1, 9, 4], 9) == 2
    assert linear_search([5, 3, 2, 1, 6], 5) == 0
    assert linear_search([-3, -1, -7], 1) == -1
    print("All tests passed")