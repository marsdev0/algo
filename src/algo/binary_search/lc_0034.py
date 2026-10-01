class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        # 先找左边界
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        first = l
        # 找右边界
        l, r = -1, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return [first, l]