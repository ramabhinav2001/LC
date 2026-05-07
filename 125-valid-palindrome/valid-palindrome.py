class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s.lower():
            if i>="a" and i<="z" or i>='0' and i<="9":
                a+=i
        return a[:]==a[::-1]
                
        