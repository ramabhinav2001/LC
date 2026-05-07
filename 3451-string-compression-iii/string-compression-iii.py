class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0

        while i < len(word):
            char = word[i]
            count = 0

            while i < len(word) and word[i] == char:
                count += 1
                i += 1

            while count > 9:
                comp += "9" + char
                count -= 9

            if count > 0:
                comp += str(count) + char

        return comp

                
