"""
Problem : Find the Smallest Element in an Array
Pattern : Traversal

Approach (apne shabdon mein):
  1. Create a variable and store the minimum value
  2. Iterate the loop and return the value 

Time  : O(N)
Space : O(1)
"""


def smallest(nums):
    mini = float('inf')
    n = len(nums)
    for i in range(0, n):
        mini = min(mini, nums[i])

    return mini 


if __name__ == "__main__":
    assert smallest([3, 1, 9, 4]) == 1
    assert smallest([5]) == 5
    assert smallest([-3, -1, -7]) == -7
    print("All tests passed")