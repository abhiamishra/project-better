'''My initial thoughts:
- condition: value has to appear at least twice
- what makes it false: distinct
- set always keep things distinct...if set length < array length
'''
class Solution(object):
    def containsDuplicate(self, nums):
        return (len(set(nums))) != len(nums)
        # you can use length on set + if boolean output is present, binary operators can be used w/o explicitly writing them