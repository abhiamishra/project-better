'''My initial thoughts:
- if t is an anagram: what does being an anagram mean?
- the same letters and the same count of letters.
- first thought that comes to my head utilizes dictionaries:
    - you can store count and the list of keys is a set
'''
class Solution(object):
    def isAnagram(self, s, t):
        dictS, dictT = {}, {}
        for sLetter in s:
            dictS[sLetter] = dictS.get(sLetter, 0) + 1
        for tLetter in t:
            dictT[tLetter] = dictT.get(tLetter, 0) + 1
        return dictS == dictT


'''Notes:
- You can compare dictionaries with ==
- There is a far better solution with set. Utilize set.count() -> functions just like a dictionary key-value pair'''