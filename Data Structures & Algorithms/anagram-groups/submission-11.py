class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalHashMap = {}
        for i in range(0,len(strs)):
            sortedWord = tuple(sorted(strs[i]))
            if sortedWord in finalHashMap:
                finalHashMap[sortedWord].append(strs[i])
            else:
                finalHashMap[sortedWord] = [strs[i]]
        return list(finalHashMap.values())
        