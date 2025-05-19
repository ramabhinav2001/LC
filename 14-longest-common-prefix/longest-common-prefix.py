class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        n=len(strs)
        character=""
        for i in range(len(strs[0])):
            character=strs[0][i]
            for j in strs[1:]:
                if i==len(j) or character != j[i]:
                    return strs[0][:i]
        return strs[0]
        
            
            