# 堆 / 优先队列      

## 如何手写一个堆   
堆的基本操作：
1. 插入一个数 
2. 求集合中的最小(大)值
3. 删除最小(大)值
4. 删除任意一个元素
5. 修改任意一个元素

堆其实是一个完全二叉树，一维数组就可以存储一个堆。    
以小根堆为例：   
每个节点都是小于等于左右孩子的，heap表示对，size表示当前堆的大小，下标从1开始；    
如果下标从0开始，存在一个问题，0位置的左孩子还是0。

操作：
1. 操作一个数：`heap[++size] = k; up(size)`
2. 求集合中的最小值：`heap[1]`
3. 删除最小值：`heap[1] = heap[size]; size--; down(1)`
4. 删除任意一个元素，假设要删除第k个节点：`heap[k] = heap[size]; size--; donw(k); up(k)`
5. 修改任意一个元素：`heap[k] = x; down(k); up(k)`

down和up，同时只会执行一个，因此，在删除任意一个元素的逻辑中，可以都写上

## Java 模板

### 最小堆  

```java
// 以最小堆为例
void down(int u) {
    int t = u;
    if (u * 2 <= size && heap[u * 2] < heap[t]) {
        t = u * 2;
    }
    if (u * 2 + 1 <= size && heap[u * 2 + 1] < heap[t]) {
        t = u * 2 + 1;
    }
    if (t != u) {
        swap(heap, t, u);
        down(t);
    }
}

void up(int u) {
    while (u / 2 > 0 && heap[u / 2] > heap[u]) {
        swap(heap, u / 2, u);
        u /= 2;
    }
}
```   

### 最大堆     
```java 

```


## 易错点

- TODO

## 代表题目

- TODO
