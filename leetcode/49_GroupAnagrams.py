class Solution:
    '''
    n = number of strings
    s = length of strings
    Time Complexity = O(n*slog(s))
    Space Complexity = O(2s)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        result = [values for values in anagrams.values()]

        return result