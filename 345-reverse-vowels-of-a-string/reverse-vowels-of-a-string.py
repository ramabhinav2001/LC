class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=["a","A","e","E","i","I","o","O","u","U"]
        n=len(s)
        rev_s=s[::-1]
        rev_ord=[]
        for i in range(n):
            if rev_s[i] in v:
                rev_ord.append(rev_s[i])
        k=0
        s_list=list(s)
        for j in range(n):
            if s_list[j] in v:
                s_list[j]=rev_ord[k]
                k +=1
        return "".join(s_list)