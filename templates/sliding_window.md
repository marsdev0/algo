# 滑动窗口

滑动窗口可以归为快慢指针，一快一慢两个指针前后相随，中间的部分就是窗口。滑动窗口算法技巧主要用来解决子数组问题，例如：查找符合某个条件的最长、最短子数组。

## 定长滑窗    
窗口右端点在 `i` 时，由于窗口大小为 `k` ，所以窗口左端点为 `i - k + 1` 。   
三步走：入 -> 更新 -> 出
1. 入：下标为 `i` 的元素进入窗口，更新相关统计量。如果窗口左端点 `i - k + 1 < 0`，则尚未形成第一个窗口，重复第一步
2. 更新：更新答案
3. 出：下标为 `i - k + 1` 的元素离开窗口，更新相关统计量，为下一个循环做准备

以上三步适用于所有定长滑动窗口题目，由于是定长，因此不需要收缩窗口，只需要当符合窗口大小时，不断更新数据，然后出窗口。

### Java 模板

```java
public int fixedWindow(int[] nums, int k) {
    // 视题型初始化：求最大 Integer.MIN_VALUE，求最小 Integer.MAX_VALUE，计数 0
    int result = ...;

    for (int right = 0; right < nums.length; right++) {
        // 右端点进入窗口
        add(nums[right]);

        int left = right - k + 1;
        if (left < 0) {
            continue;
        }

        // 更新逻辑
        result = update(result);

        // 左端点出窗口
        remove(nums[left]);
    }
    return result;
}
```   

### Python 模板

```python
def fixed_window(nums: list[int], k: int) -> int:
    # 视题型初始化：求最大 float("-inf")，求最小 float("inf")，计数 0
    result = ...

    for right in range(len(nums)):
        # 右端点进入窗口
        add(nums[right])

        left = right - k + 1
        if left < 0:
            continue

        # 更新逻辑
        result = update(result)

        # 左端点出窗口
        remove(nums[left])

    return result
```

## 不定长滑窗         
主要在于什么时候收缩窗口   
- 求最大、最长，例如：元素之和小于 `target` 的最大长度
- 求最小、最短，例如：元素之和大于 `target` 的最小长度

### Java 模板     
```java  
// 求最大
public int longestWindow(int[] nums, int target) {
    int sum = 0;
    int left = 0;
    int maxLen = 0;
    
    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            sum -= nums[left];
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}

// 求最小
public shortestWindow(int[] nums, int target) {
    int sum = 0;
    int left = 0;
    int minLen = 0x3f3f3f3f;
    
    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            minLen = Math.min(minLen, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }
    return minLen == 0x3f3f3f3f ? -1 : minLen;
}
```     

### Python 模板   
```python  
# 求最大
def longest_window(nums: list[int], target: int) -> int:
    total = 0
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            total -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

# 求最小   
def shortest_window(nums: list[int], target: int) -> int:
    total = 0
    left = 0
    min_len = 0x3f3f3f3f

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    
    return min_len if min_len != 0x3f3f3f3f else -1   
```   


## 易错点

- “入 -> 更新 -> 出”的顺序不能乱：更新时读到的统计量必须是完整的 k 个元素，先出再更新会把窗口少算一个
- `result` 初始值随题型变化：求最大用极小值、求最小用极大值、计数用 0
- Java 求和注意溢出：元素大时统计量用 `long`（如 2461）
- 答案要求下标时记的是左端点 `left = right - k + 1`
- 判断平均值用乘法代替除法（如 1343：`total >= k * threshold`），避免精度问题

## 代表题目

- 643 子数组最大平均数 I（求和最大）
- 1343 大小为 K 且平均值大于等于阈值的子数组数目（计数）
- 1456 定长子串中元音的最大数目（计数）
- 2461 长度为 K 的子数组中的最大和（求和，注意 long）
- 438 找到字符串中所有字母异位词（计数 + 哈希维护）
