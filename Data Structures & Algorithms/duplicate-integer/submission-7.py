class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        isDuplicated = False
        for i in nums:
            if i == prev:
                isDuplicated = True
                break
            else:
                prev = i
        return isDuplicated