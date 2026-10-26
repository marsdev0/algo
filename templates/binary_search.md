# 二分查找

在单调性上折半查找答案或边界。核心是维护**不变量**：循环中每一步都保证"答案在当前区间内"。

## Python 模板

与 `src/algo/binary_search/__init__.py` 保持一致。

```python
def binary_search_exact(nums: list[int], target: int) -> int:
    """模板一：精准匹配，闭区间 [left, right]"""
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


def binary_search_left(nums: list[int], target: int) -> int:
    """模板二：左边界，第一个 >= target 的下标，左闭右开 [left, right)"""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  # == len(nums) 表示不存在


def binary_search_right(nums: list[int], target: int) -> int:
    """模板三：右边界，最后一个 <= target 的下标，开区间 (left, right]"""
    left, right = -1, len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2  # 上取整，防死循环
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left
```

## Java 模板

```java
public class BinarySearchTemplates {

    /** 模板一：精准匹配，闭区间 [left, right] */
    public static int searchExact(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }

    /** 模板二：左边界，第一个 >= target 的下标，左闭右开 [left, right) */
    public static int searchLeft(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left; // == nums.length 表示不存在
    }

    /** 模板三：右边界，最后一个 <= target 的下标，开区间 (left, right] */
    public static int searchRight(int[] nums, int target) {
        int left = -1, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2; // 上取整，防死循环
            if (nums[mid] <= target) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```

## 易错点

- Java 中 `mid` 用 `left + (right - left) / 2` 防溢出；Python 无此问题
- 模板三的 `mid` 必须**上取整**，否则 `left = mid` 会死循环
- 模板二/三的返回值可能越界（`len` 或 `-1`），调用方必须判断
- 看到"最大化最小值 / 最小化最大值"→ 二分答案

## 代表题目

- 34 查找元素的第一个和最后一个位置（模板二 + 三）
- 704 二分查找（模板一）
- 2563 统计公平数对的数目（排序后枚举 + 边界二分）
