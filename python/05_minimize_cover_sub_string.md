## 题目：
### ☆名称： 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

**注意：**
- 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
- 如果 s 中存在这样的子串，我们保证它是唯一的答案。

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
```
**示例 2：**
```
输入：s = "a", t = "a"
输出："a"
```
**示例 3：**
```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

*☆提示：*
- $$1 <= s.length, t.length <= 10^5$$
- s 和 t 由英文字母组成

**结果:**

[算法思路]：
1. 窗口即切片，在s中找到一个切片，我们希望t中的元素都在该切片中出现，并使这个切片尽可能短。

2. 滑动窗口，用右边界来一步一步探索s，做到不遗漏。当右边界达到某个值时满足条件，开始压缩左边界，尽可能使得切片变得更短且不破坏刚刚满足的条件。

3. 代码含义：根据目标t字符串，建立need_dict和need_cnt，为什么要这样建立？设想你该如何滑动左边界且验证当前的切片是否会破坏条件？如果使用线性遍历切片，这个地方你得花O（N），那么总的时间复杂度将从O（N）退化到O（N^2）。而使用一个字典和计数变量可以以O（1）形式判断该切片是否依旧满足条件。

4. needMap 代表：需要某个字符（key）若干个（value). needCnt表示当前缺失的字符数量。

线性遍历s，当遍历的字符在needMap中，对该字符的需要的数量减1，那么needCnt可以减1吗？不行，比如你需要"ab", 此时你遇到了两个“a”，因此needMap[a] = -1，needMap[b] = 1, 说明你不需要a了，但你仍然需要b，所以更新needCnt的方式为：
```python
if s[j] in needMap:
    if needMap[s[j]] > 0:
        needCnt -= 1
    needMap[s[j]] -= 1
```


[最终代码]：
```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left_index = right_index = 0 
        need_dict = dict()
        need_cnt = len(t)
        rst = ""
        for i in range(len(t)):
            if t[i] not in need_dict: need_dict[t[i]] = 1
            else: need_dict[t[i]] += 1
        print(need_dict)
        for right_index in range(len(s)):
            if s[right_index] in need_dict:
                if need_dict[s[right_index]] > 0:
                    need_cnt -= 1
                need_dict[s[right_index]] -= 1

            while need_cnt == 0:
                print(left_index)
                if not rst or right_index - left_index + 1 < len(rst):
                    rst = s[left_index : right_index + 1]
                
                if s[left_index] in need_dict:
                    print("inin")
                    if need_dict[s[left_index]] == 0:
                        need_cnt += 1
                    need_dict[s[left_index]] += 1
                left_index += 1
        return rst
```