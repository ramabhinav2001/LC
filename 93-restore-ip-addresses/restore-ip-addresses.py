class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n=len(s)
        ans=[]
        def valid(chunk):
            if len(chunk)>1 and chunk[0]=="0":
                return False
            return 0<=int(chunk)<=255
        
        def backtracking(start,parts):
            if len(parts)==4:
                if start==n:
                    ans.append(".".join(parts))
                return
            rem_parts=4-len(parts)
            rem_chars=n-start
            if not(rem_parts<=rem_chars<=3*rem_parts):
                return

            for end in range(start+1,min(start+3,n)+1):
                part=s[start:end]
                if valid(part):
                    parts.append(part)
                    backtracking(end,parts)
                    parts.pop()
        
        backtracking(0,[])
        return ans
