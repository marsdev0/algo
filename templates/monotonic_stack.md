# 单调栈

在栈的基础上，维持一个栈内元素单调；   
题目类型比较单一，有如下几种：
1. 查找元素A左侧第一个比它大的元素
2. 查找元素A左侧第一个比它小的元素
3. 查找元素A右侧第一个比它大的元素
4. 查找元素A右侧第一个比它小的元素

总结：
1. 比它大 -> **使用单调减**
2. 比它小 -> **使用单调增**
3. 左侧右侧，有两种写法，顺序和逆序，这两种写法只是相对的参考不一样
4. ans数组元素默认值为-1
5. **求左侧，判断时加上等于；求右侧，判断时不加等于**

## 元素A左侧第一个比它大的元素   
```java
int[] leftLarge(int[] nums, int n) {
    int[] ans = new int[n];
    Arrays.fill(ans, -1);
    Stack<Integer> st = new Stack<>();

    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && nums[i] >= nums[st.peek()]) {
            st.pop();
        }
        // 关注与右侧的区别
        if (!st.isEmpty()) {
            // 这里是peek，不是pop
            ans[i] = nums[st.peek()];
        }
        st.push(i);
    }
    return ans;
}
```

## 元素A左侧第一个比它小的元素  
```java
int[] leftSmall(int[] nums, int n) {
    int[] ans = new int[n];
    Arrays.fill(ans, -1);
    Stack<Integer> st = new Stack<>();

    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && nums[i] <= nums[st.peek()]) {
            st.pop();
        }
        // 关注与右侧的区别
        if (!st.isEmpty()) {
            // 这里是peek，不是pop
            ans[i] = nums[st.peek()];
        }
        st.push(i);
    }
    return ans;
}
```

## 元素A右侧第一个比它大的元素     
```java
int[] rightLarge(int[] nums, int n) {
    int[] ans = new int[n];
    Arrays.fill(ans, -1);
    Stack<Integer> st = new Stack<>();

    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && nums[i] > nums[st.peek()]) {
            // 关注与左侧的区别
            ans[st.pop()] = nums[i];
        }
        st.push(i);
    }
    return ans;
}
```

## 元素A右侧第一个比它小的元素   
```java
int[] rightSmall(int[] nums, int n) {
    int[] ans = new int[n];
    Arrays.fill(ans, -1);
    Stack<Integer> st = new Stack<>();

    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && nums[i] < nums[st.peek()]) {
            // 关注与左侧的区别
            ans[st.pop()] = nums[i];
        }
        st.push(i);
    }
    return ans;
}
```


## 易错点

- **求左侧时取答案用 `peek()` 而不是 `pop()`**：栈顶元素还可能是后续元素的答案，弹掉会导致后面答案错误（如 `[5,3,4]` 中 4 的答案应仍是 5）
- 求左侧、求右侧两类写法的核心区别：
  - 求左侧：当前元素 i 出栈条件加 `=`，答案在 while 之后从栈顶 `peek` 读出
  - 求右侧：当前元素 i 出栈条件不加 `=`，答案在 while 内部出栈时写入
- Java 建议用 `Deque<Integer> st = new ArrayDeque<>()` 代替 legacy 的 `Stack`（后者继承 Vector，方法加锁，性能差）
- 若返回下标而非值，信息更全（值可由下标推出，反之不行），更通用

## 代表题目

- TODO
