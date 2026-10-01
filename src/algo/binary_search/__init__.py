"""
二分法模板
"""

def binary_search_1(nums: list[int], target: int) -> int:
    """精准匹配"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binary_search_2(nums: list[int], target: int) -> int:
    """左边界"""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def binary_search_3(nums: list[int], target: int) -> int:
    """右边界"""
    left, right = -1, len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left