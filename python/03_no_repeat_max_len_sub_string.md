## 题目：
### ☆名称： 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

**示例 1：**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
**示例 2：**
```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
**示例 3：**
```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

*☆提示：*
- 0 <= s.length <= 5 * 104
- s 由英文字母、数字、符号和空格组成

**结果:**
- **暴力解法：**

遍历所有可能的不重复子串，取所有不重复子串中最大长度并返回。
时间复杂度：$$O(n^2)$$
[代码]：
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            rst = 0
            temp = list()
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                    rst += 1
                else:
                    break 
            result = max(result, rst)
        return result 
```

- **滑动窗口解法：**

什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：$$O(n)$$
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = temp_len = 0
        temp_set = set()
        left = 0
        for i in range(len(s)):
            temp_len += 1
            while s[i] in temp_set:
                temp_set.remove(s[left])
                left += 1
                temp_len -= 1
            max_len = max(max_len, temp_len)
            temp_set.add(s[i])
        return max_len
```