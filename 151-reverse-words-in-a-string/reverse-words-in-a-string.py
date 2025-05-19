class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reversearr(arr):
            x=[]
            for i in range(len(arr)-1,-1,-1):
                x.append(arr[i])
            return x

        arrstring=s.strip().split()
        revsen=" ".join(reversearr(arrstring))
        return revsen


