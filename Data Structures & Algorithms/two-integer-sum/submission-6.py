class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This solution is considered as better solution since it's O(n) whereas the one that I used (nested loop) is O(n²).
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i