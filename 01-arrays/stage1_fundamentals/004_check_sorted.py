"""
Problem : Check if an Array Is Sorted
Pattern : Traversal

Approach (apne shabdon mein):
  1. Iterate the list, Start from index 1.
  2. If i'th element is greater than i-1'th element then array is sorted.

Time  : O(N)
Space : O(1)
"""


def check_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False

    return True


if __name__ == "__main__":
    assert check_sorted([1, 2, 3, 4, 5]) == True
    assert check_sorted([1, 2, 2, 3, 4]) == True
    assert check_sorted([5, 4, 3, 2, 1]) == False
    assert check_sorted([1, 3, 2, 4]) == False
    assert check_sorted([5]) == True
    assert check_sorted([]) == True

    print("All tests passed")