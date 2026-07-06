class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = []
        isPresent = False
        for i in nums:
            if i in new_array:
                isPresent = True
                break
            else:
                new_array.append(i)
        return isPresent