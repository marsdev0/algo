# 二叉树

## 前序遍历    
```java
class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;
}

List<Integer> ans = new ArrayList<>();
// 递归  
void preOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    ans.add(root.value);
    preOrder(root.left);
    preOrder(root.right);
} 


// 非递归   
void preOrder(TreeNode root) {
    if (root == null) {
        return;
    } 
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);

    while (!stack.isEmpty()) {
        TreeNode cur = stack.pop();
        ans.add(cur.val);
        if (cur.right != null) {
            stack.push(cur.right);
        }
        if (cur.left != null) {
            stack.push(cur.left);
        }
    }
}
```

## 中序遍历    
```java
List<Integer> ans = new ArrayList<>();

// 递归
void inOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    inOrder(root.left);
    ans.add(root.val);
    inOrder(root.right);
}

// 非递归 左中右
void inOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    Dequeu<TreeNode> stack = new ArrayDeque<>();
    TreeNode cur = root;

    while (!stack.isEmpty() || cur != null) {
        // if (cur != null) {
        //     stack.push(cur);
        //     cur = cur.left;
        // } else {
        //     cur = stack.pop();
        //     ans.add(cur.val);
        //     if (cur.right != null) {
        //         cur = cur.right;
        //     }
        // }
        while (cur != null) {
            // 沿着左子树一直向下压
            stack.push(cur);
            cur = cur.left;
        }
        cur = stack.pop();
        ans.add(cur.val);
        cur = cur.right;
    }
}
```


## 后序遍历   
```java
List<Integer> ans = new ArrayList<>();

// 递归
void postOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    postOrder(root.left);
    postOrder(root.right);
    ans.add(root.val);
}

// 非递归 - 方案一：中右左 -> 反转为左右中
void postOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);

    while (!stack.isEmpty()) {
        TreeNode cur = stack.pop();
        ans.add(cur.val);
        if (cur.left != null) {
            stack.push(cur.left);
        }
        if (cur.right != null) {
            stack.push(cur.right);
        }
    }
    Collections.reverse(ans);
}

// 非递归 - 方案二：栈 + prev指针
// 当某个节点的右子树已经访问完成，即 node.right == prev，才访问该节点
// 否则说明右子树没有处理完成，得先转向右子树
void postOrder(TreeNode root) {
    if (root == null) {
        return;
    }
    Deque<TreeNode> stack = new ArrayDeque<>();
    TreeNode prev = null;
    TreeNode cur = root;

    while (!stack.isEmpty() || cur != null) {
        while (cur != null) {
            stack.push(cur);
            cur = cur.left;
        }
        TreeNode node = stack.peek();
        // 右子树为空 或者 右子树已经访问过
        if (node.right == null || node.right == prev) {
            ans.add(node.val);
            prev = node;
            stack.pop();
        } else {
            cur = cur.right;
        }
    }
}
```

## 层次遍历   



## 易错点

- TODO

## 代表题目

- TODO
