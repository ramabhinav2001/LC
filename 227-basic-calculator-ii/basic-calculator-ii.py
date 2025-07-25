class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sign = "+"
        stack = []
        s = s.replace(" ", "")

        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i==len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    stack.append(int(prev / num)) if prev >= 0 else stack.append(-(-prev // num))
                num = 0
                sign = ch

        return sum(stack)