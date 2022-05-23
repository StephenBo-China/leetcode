## 题目：
### ☆名称： 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

**示例 1：**

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```
**示例 2：**
```
输入：target = 4, nums = [1,4,4]
输出：1
```
**示例 3：**
```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

**结果:**

[算法思路]：
1. 因为nums中都是正整数，因而右边界逐渐向右过程中滑动窗口内的和是不断增大的，左边界向右的过程中滑动窗口内的和是不断减小的。
2. 因而套用滑动窗口类题目解题思路，先让右边界逐渐扩大，直到窗口内的值得和大于了target，开始移动左边界，直到窗口内的和小于target为止，此时倒数第二次移动左边界的窗口即是当前的最小大于等于target的最小窗口，将其记录。
3. 重复1、2直到右边界到头为止。

[最终代码]：
```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        rst = float('inf')
        start,end = 0, 0
        sum = 0 
        while end < len(nums):
            sum += nums[end]
            if sum >= target:
                while sum >= target:
                    sum -= nums[start]
                    start += 1
                rst=min(rst,end - (start - 1) + 1)
                print(start + 2, ",", end)
            end += 1
        if rst==float('inf'): 
            return 0
        else: 
            return rst
```