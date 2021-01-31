'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tmp_dict = dict()
    for i in range(len(nums)):
        if target - nums[i] not in tmp_dict:
            tmp_dict[nums[i]] = i
        else:
            return [tmp_dict[target - nums[i]], i]
    return []


def main():
    nums = [2, 7, 11, 5]
    target = 9
    print(twoSum(nums, target))

if __name__ == '__main__':
    main()
