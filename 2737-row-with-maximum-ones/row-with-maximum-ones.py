class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        count=0
        ind={}
        realc=0
        for i in range(len(mat)):
            count=0
            for j in mat[i]:
                if j==1:
                    count +=1
            realc=max(realc,count)
            ind[i]=count
        c=0
        min_key=float("inf")
        for k,v in ind.items():
            if realc==v:
                x=k
                c +=1
                min_key=min(min_key,k)
        
        return [min_key,realc]