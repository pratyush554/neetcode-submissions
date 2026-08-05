class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        finalHashMap = {}
        for i in nums:
            if i in finalHashMap:
                finalHashMap[i] += 1
            else:
                finalHashMap[i] = 1
        
        sortedNumbers = sorted(
            finalHashMap,
            key=finalHashMap.get,
            reverse=True
        )

        return sortedNumbers[:k]