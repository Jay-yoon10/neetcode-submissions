class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            print("i", i)
            for j in range(len(nums)-1, 0,-1):
                if nums[i] + nums[j] == target and i != j:
                    output.append(i)
                    output.append(j)
                    return output   
        return output
