class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrayStorage = []
        for i in range(0, len(nums)):
            if nums[i] not in arrayStorage:
                arrayStorage.append(nums[i])
            else:
                return True
        return False       

        