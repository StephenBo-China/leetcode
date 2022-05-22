## 题目：
### ☆名称： 至多包含两个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

**示例 1：**

```
输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
```
**示例 2：**
```
输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。
```

**结果:**

[算法思路]：
1. 逐步向右移动滑动窗口的右边界，如果满足至多包含2个字符则继续移动；如果不满足则开始移动左边界直到满足条件为止；
2. 右边界移动过程中去判断当下满足条件的滑动窗口内子串长度是否是当前最长情况，是的话则改变结果的长度。


[最终代码]：
```python
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        rst = float("-inf")
        temp = ""
        for right in range(len(s)):
            sub_string = s[left:(right + 1)]
            temp_set = set()
            for i in sub_string:
                temp_set.add(i)
            if len(temp_set) <= 2:
                rst = max(rst, len(sub_string))
                temp = sub_string
            else:
                while left < right:
                    sub_string = s[left:(right + 1)]
                    temp_set = set()
                    for i in sub_string:
                        temp_set.add(i)
                    if len(temp_set) <= 2:
                        break
                    left += 1
        return rst
```