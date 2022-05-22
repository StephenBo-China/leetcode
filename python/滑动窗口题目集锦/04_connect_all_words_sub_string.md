## 题目：
### ☆名称： 串联所有单词的子串
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

**示例 1：**

```
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
```
**示例 2：**
```
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
```
**示例 3：**
```
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
```

*☆提示：*
- $$1 <= s.length <= 10^{14}$$
- s 由小写英文字母组成
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- words[i] 由小写英文字母组成

**结果:**

1. 总共用到两个哈希表，all_words_dict 用于记录words中单词出现的次数，temp_words_dict 用于记录子串中（也就是滑动窗口中）单词出现的次数
2. word_num 为单词的个数，word_len为单词长度
3. 遍历字符串，移动长度为 word_num * word_len 的滑动窗口，再在当前滑动窗口中依次比较wordLen长度的单词
4. 当这个窗口内一旦出现不存在all_words_dict中的单词，或者这个单词在子串中出现的次数已经等于all_words_dict中的次数(也就是再加入这个子串次数就要超出了)，这个滑动窗口就不符合要求，直接break进入下一个滑动窗口的匹配
5. 一旦完全匹配上了，把滑动窗口的起始索引加入结果result中

[代码]：
```python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        word_num = len(words)
        all_words_dict = dict()
        result = list()
        for word in words:
            if word not in all_words_dict:
                all_words_dict[word] = 1 
            else:
                all_words_dict[word] = all_words_dict[word] + 1
        for i in range(0, len(s)):
            left_index = i
            right_index = i + word_len * word_num
            if right_index > len(s): break 
            sub_string = s[left_index:right_index]
            # print(sub_string)
            temp_words_dict = dict()
            for j in range(0, len(sub_string) - word_len + 1, word_len):
                word_tmp = sub_string[j:(j+word_len)]
                if word_tmp not in temp_words_dict:
                    temp_words_dict[word_tmp] = 1
                else:
                    temp_words_dict[word_tmp] = temp_words_dict[word_tmp] + 1
            judge = True 
            for word in all_words_dict:
                if word not in temp_words_dict or all_words_dict[word] != temp_words_dict[word]:
                    judge = False 
                    break 
            if judge:
                result.append(left_index)
        return result 
```