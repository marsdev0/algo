# 排序

## 快速排序
基于分治的思想：
1. 确定分界点：可以取左端点、右端点或者中间节点
2. 调整区间：存在一个 `x` 元素，使得左边所有的数都小于等于 `x`，右边所有的数都大于等于 `x`
3. 递归处理左右两段

### Java 模板
```java
void quickSort(int[] nums, int start, int end) {
    if (start >= end) {
        return;
    }
    int j = partition(nums, start, end);
    quickSort(nums, start, j);
    quickSort(nums, j+1, end);
}

// 取中间节点作为x，在退出循环后，不需要再次交换位置
int partition(int[] nums, int start, int end) {
    int x = nums[start + (end - start) / 2];
    int i = start - 1;
    int j = end + 1;

    while (true) {
        while (i <= end && nums[++i] < x);
        while (j >= start && nums[--j] > x);
        if (i >= j) {
            break;
        }
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    return j;
}
```


## 归并排序    
主要流程：
1. 先递归，当左右数组有序时，可以合并
2. 再合并

### Java 模板      
```java
void sort(int[] nums, int start, int end) {
    if (start >= end) {
        return;
    }
    int mid = start + (end - start) / 2;
    sort(nums, start, mid);
    sort(nums, mid + 1, end);
    merge(nums, start, mid, end);
}

void merge(int[] nums, int start, int mid, int end) {
    int[] arr = new int[end - start + 1];
    int i = start;
    int j = mid + 1;
    int idx = 0;
    
    while (i <= mid && j <= end) {
        if (nums[i] <= nums[j]) {
            arr[idx++] = nums[i++];
        } else {
            arr[idx++] = nums[j++];
        }
    }

    while (i <= mid) {
        arr[idx++] = nums[i++];
    }
    while (j <= end) {
        arr[idx++] = nums[j++];
    }
    for (int k = 0; k < idx; k++) {
        nums[start + k] = arr[k];
    }
}
```
