# https://leetcode.com/problems/valid-palindrome/
# simple (success)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        s = s.lower()
        s = s.replace(" ", "")
        s = [_ for _ in s if _.isalnum()]
        reverse_s = s[::-1]
        
        if s == reverse_s:
            return True
        return False
