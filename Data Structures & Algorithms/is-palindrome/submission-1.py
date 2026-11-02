class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if alphanum_str == alphanum_str[::-1]:
            return True
        else:
            return False