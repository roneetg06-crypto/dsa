"""
Problem : Reverse an Array
Pattern : Two Pointers

Approach (apne shabdon mein):
  1.
  2.

Time  : O(?)
Space : O(?)
"""


def reverse_array(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return numsc


if __name__ == "__main__":
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_array([5]) == [5]
    assert reverse_array([]) == []
    print("All tests passed")