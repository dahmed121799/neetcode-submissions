class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
                word = strs[i]
                key = ''.join(sorted(word))

                if key not in groups:
                    groups[key] = []

                groups[key].append(word)
        return list(groups.values())
                
        