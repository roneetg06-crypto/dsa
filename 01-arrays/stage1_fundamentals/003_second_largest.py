"""
Problem : Find the Second Largest in an Array
Pattern : Traversal

Approach (apne shabdon mein):
  1. First find the largest element using iterating the loop
  2. Compare each element which is smaller than first largest and greater than with second largest

Time  : O(N)
Space : O(1)
"""


def second_largest(nums):
    n = len(nums)
    first_large = float('-inf')
    second_large = float('-inf')
    for i in range(0, n):
        first_large = max(first_large, nums[i])

    for i in range(0, n):
        if first_large > nums[i] and second_large < nums[i]:
            second_large = nums[i]

    if second_large != float('-inf'):
        return second_large
    else:
        return None
    

if __name__ == "__main__":
    assert second_largest([3, 1, 9, 4]) == 4
    assert second_largest([5]) == None
    assert second_largest([-3, -1, -7]) == -3
    print("All tests passed")