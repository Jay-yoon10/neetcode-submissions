class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isValid = True
        array1 = sorted(s)
        array2 = sorted(t)
        if len(s) != len(t):
            isValid = False
            return isValid
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                isValid = False 


        return isValid