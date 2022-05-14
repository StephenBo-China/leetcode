## 题目：
### ☆名称： 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

<img src="https://stephen-bo-data-store-1311928953.cos.ap-beijing.myqcloud.com/two_add.png" style="zoom:75%" />

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```
**示例 2：**
```
输入：l1 = [0], l2 = [0]
输出：[0]
```
**示例 3：**
```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```

**结果:**

由于链表的顺序刚好是从个位数开始加，则链表对应位置数相加后跟10取余的数刚好为对应位置的数字，跟10相除取整后刚好是向前进的那一位的数字。十位数为十位数两链表对应位置的数字相加后再加上进的那一位数字（往前进的那一位数字可以是0）。
如果一个链表的长度短于另一个链表，则证明短的链表位数不足，不足的地方相当于直接加上0（补0）。

- 边界case：
如果最大的位数相加后除以10大于0，这时两链表均已遍历完成，但需要将除以10大于0的部分向前进一位放到结果链表中。

[整体思路如下图]：

<img src="https://stephen-bo-data-store-1311928953.cos.ap-beijing.myqcloud.com/temp.png" style="zoom:50%" />

[代码]：
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = b = ListNode(None)
        tmp = 0
        while l1 is not None or l2 is not None or tmp != 0:
            l1_v = l2_v = 0
            if l1 is not None: l1_v = l1.val 
            if l2 is not None: l2_v = l2.val 
            tmp = tmp + l1_v + l2_v
            b.next = ListNode(tmp % 10)
            b = b.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            tmp = tmp // 10
            # l1 = l1.next
            # l2 = l2.next
        return a.next 

```