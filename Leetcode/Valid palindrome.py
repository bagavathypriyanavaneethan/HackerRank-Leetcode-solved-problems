class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Removing the special characters & then lowering the string
        a = "".join(c for c in s if c.isalnum())
        a = a.lower()
        
        #Reversing the string
        b = a[::-1]
        
        if a == b:
            return True
        else:
            return False
        
