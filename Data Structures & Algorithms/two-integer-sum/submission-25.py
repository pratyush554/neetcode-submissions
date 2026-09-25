class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storeTable = {}
        for i in range(0,len(nums)):
            valueToCheck = target - nums[i]
            if valueToCheck in storeTable:
                return [storeTable[valueToCheck],i]
            storeTable[nums[i]] = i
        return []