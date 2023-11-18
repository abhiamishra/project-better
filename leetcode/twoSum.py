'''
- two indices that when accessed: equal target
- each input has only one pair of indices = target
- cannot use the same element twice
- initial thought:  divide in half, take elem in their and find their counterparts in the rest of hte list
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            remainNum = target - nums[i]
            
            if remainNum in nums:
                index = nums.index(remainNum)
                if index != i:
                    return [i, index]

'''
Better solution involves using dictionary instead of using .index()
Research time complexity of .index()
    - O(n) since it goes over the entire list
Dictionary is O(1) since each number is logged into as the key and it is O(1) to search up
'''

        
# BETTER EFFICIENT SOLUTION:
'''
- two indices that when accessed: equal target
- each input has only one pair of indices = target
- cannot use the same element twice
- initial thought: sort, divide in half, take elem in their and find their counterparts in the rest of hte list
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictNums = {}
        for i in range(0, len(nums)):
            remainNum = target - nums[i]
            if remainNum in dictNums:
                return [dictNums[remainNum], i]
            
            dictNums[nums[i]] = i
        