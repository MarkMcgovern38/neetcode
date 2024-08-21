class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in sorted_strings:
                sorted_strings[sorted_word] = [i]
            else:
                sorted_strings[sorted_word].append(i)
        return list(sorted_strings.values()) 