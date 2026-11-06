# Trie树

## 是什么
Trie树，也叫前缀树、字典树，用于**快速查询某个字符串**或者**字符前缀是否存在**的数据结构

作用：高效地**存储**和**查找**字符串集合的数据结构

核心性质：
1. 根节点不包含字符，除根节点外每个节点都包含一个字符
2. 从根到某节点的路径就是该节点对应的字符串或前缀
3. 每个节点的所有子节点代表的字符各不相同
4. 通常在单词结尾打上一个结束标记


凡是用Trie树，一般题目中肯定限制了字母只有26或52个（字符集大小决定每个节点的分支数）

时间复杂度：
插入：O(L)，L为字符串长度
查询：O(L)
前缀查询：O(L)

应用场景：
1. 搜索引擎自动补全：输入前缀 -> 列出所有候选词
2. 拼写检查：快速判断单词是否在词典中
3. IP路由（最长前缀匹配）：网络设备转发数据包
4. 九宫格输入法：数字序列 -> 候选词
5. 单词游戏：Boggle、Scrabble 中的合法词判断
6. 最大异或对：把数字按二进制塞入 01-Trie


## 实现方式一：节点方案   
每个节点是一个对象，子节点用数组存储

```java
class Trie {
    class TrieNode {
        boolean end;
        TrieNode[] children = new TrieNode[26];
    }

    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    void insert(String word) {
        TrieNode p = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            TrieNode child = p.children[index];
            if (child == null) {
                child = new TrieNode();
                p.children[index] = child;
            }
            p = child;
        }
        p.end = true;
    }

    boolean search(String word) {
        TrieNode p = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            TrieNode child = p.children[index];
            if (child == null) {
                return false;
            }
            p = child;
        }
        return p.end;
    }

    boolean startWith(String word) {
        TrieNode p = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            TrieNode child = p.children[index];
            if (child == null) {
                return false;
            }
            p = child;
        }
        return true;
    }
}
```    

## 实现方式二：数组
