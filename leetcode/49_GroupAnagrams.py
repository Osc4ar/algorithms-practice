class Solution:
    '''
    We can create a dictionary where the key is a sorted string and the value is a list of anagrams 

    1. For every string we do:
        1. Sort the string, that will be the key
        2. If the key already exists, append the string to that list
        3. If it does not exist, add it to the dictionary with a new list with the string as its single value
    2. Return a list with all the lists saved on the dictionary
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)

        return [group for group in anagrams.values()]
