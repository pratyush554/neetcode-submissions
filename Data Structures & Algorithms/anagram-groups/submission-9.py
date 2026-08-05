class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sortedWord = tuple(sorted(word))

            if sortedWord in groups:
                groups[sortedWord].append(word)
            else:
                groups[sortedWord] = [word]

        return list(groups.values())