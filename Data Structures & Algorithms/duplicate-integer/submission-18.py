class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNumbers = set()
        for i in nums:
            if i in setOfNumbers:
                return True
            setOfNumbers.add(i)
        return False