#initial thoughts
# we are grouping based of amount of words and type of words
# dictionary where the key is the rep of the set and the value is the set
# check whether there is a set difference between the list of keys
# Worst case: O(n^2)

# What optimization exists?:
# What is taking the most amount of time?
    # - 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Approach #1
        dictSet = {}
        for word in strs:
            newWord = "".join(sorted(word)) #bottleneck
            # "tea" -> 't' 'e' 'a'
            #the default option in for dictionaries is RAPID fast.
            # O(n) goes to O(1)
            #A1:
            '''if newWord in dictSet.keys(): 
                    lst = dictSet[newWord]
                    lst.append(word)
                    dictSet[newWord] = lst
                else:
                    dictSet[newWord] = [word]
            '''
            #A2
            lst = dictSet.get(newWord, [])
            lst.append(word)
            dictSet[newWord] = lst
        
        return list(dictSet.values())
'''The Python defaultdict type behaves almost exactly like a regular Python dictionary, 
but if you try to access or modify a missing key, then defaultdict will automatically 
create the key and generate a default value for it.
This makes defaultdict a valuable option for handling missing keys in dictionaries.

Also use .setdefault!'''

