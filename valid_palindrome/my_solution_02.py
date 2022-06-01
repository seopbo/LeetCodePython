# https://leetcode.com/problems/valid-palindrome/
# recursive-call (fail) -> s가 매우 긴 str일 때, 재귀호출은 스택이 쌓여서 통과를 못함.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        s = s.lower()
        s = s.replace(" ", "")
        s = [_ for _ in s if _.isalnum()]

        def check(s):
            if len(s) == 0 or len(s) == 1:
                return True
            if s[0] == s[-1]:
                return check(s[1:-1])
            else:
                return False
        return check(s)
