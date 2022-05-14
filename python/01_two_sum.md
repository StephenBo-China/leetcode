## 题目：
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

**示例 1：**
```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```
**示例 2：**
```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```
**示例 3：**
```
输入：nums = [3,3], target = 6
输出：[0,1]
```

**结果:**

使用字典存储nums中已经遍历过的元素，然后用target减去当前遍历元素，检查是否在字典中。
- 如果在：则证明nums存在两数之和为target
- 如果遍历完所有nums后，都没有找到字典中记录元素加上所有遍历元素为target，则nums没有两数之和为target。
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dp = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dp:
                return [dp[temp], i]
            dp[nums[i]] = i
        return []
```