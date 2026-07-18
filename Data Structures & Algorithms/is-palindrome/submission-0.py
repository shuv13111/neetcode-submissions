class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_arr = []
        for letters in s:
            if letters != ' ' and letters.isalnum():
                s_arr.append(letters.lower())
        if s_arr == s_arr[::-1]:
            return True
        else:
            return False