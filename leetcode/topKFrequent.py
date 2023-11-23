# initial thoughts: return k most frequent elements
# make hashmap, insert value-count, parse through map and 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictSet = {}
        for n in nums:
            dictSet[n] = dictSet.get(n, 0) + 1
        sortedList = sorted(dictSet.items(), key=lambda x: x[1],reverse=True)
        outputList = [a[0] for a in sortedList[:k]]
        return outputList