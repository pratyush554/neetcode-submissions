class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storeTable = {}
        for i in range(0,len(nums)):
            if target - nums[i] in storeTable:
                return [storeTable[target-nums[i]],i]
            storeTable[nums[i]] = i
        return []