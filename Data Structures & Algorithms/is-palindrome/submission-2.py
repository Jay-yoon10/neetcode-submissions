class Solution:
    def isPalindrome(self, s: str) -> bool:
        # It has higher complexity compare to two pointer solution, but readability is much simpler O(n)
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]