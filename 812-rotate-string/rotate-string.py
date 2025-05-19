class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if s==goal:
            return True
        for i in range(len(s)-1):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False