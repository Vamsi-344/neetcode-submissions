class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if news == news[::-1]:
            return True
        else:
            return False