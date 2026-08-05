class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalHashMap = {}
        for i in strs:
            sortedWord = tuple(sorted(i))
            if sortedWord in finalHashMap:
                finalHashMap[sortedWord].append(i)
            else:
                finalHashMap[sortedWord] = [i]
        return list(finalHashMap.values())
        