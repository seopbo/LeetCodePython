# https://leetcode.com/problems/valid-palindrome/
# two-pointer (success)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        s = s.lower()
        s = s.replace(" ", "")
        s = [_ for _ in s if _.isalnum()]

        i = 0
        j = len(s) - 1
        
        while True:
            if i > j:
                break
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
