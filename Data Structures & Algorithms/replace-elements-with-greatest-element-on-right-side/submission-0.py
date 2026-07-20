class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = []

        for i in range(len(arr) - 1):
            greatest = arr[i + 1]

            for k in range(i + 1, len(arr)):
                if greatest < arr[k]:
                    greatest = arr[k]

            newArray.append(greatest)

        newArray.append(-1)

        return newArray