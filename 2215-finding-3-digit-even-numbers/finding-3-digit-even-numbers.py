class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr=[]
        fin_arr=[]
        n=len(digits)
        s=0
        for i in digits:
            if i%2!=0:
                s +=1
        if s==n:
            return []
        else:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        if i!=j and i!=k and j!=k:
                            if digits[i]==0:
                                continue
                            nums=digits[i]*100+digits[j]*10+digits[k]
                            if nums%2==0:
                                arr.append(nums)
            fin_arr=sorted(set(arr))
            return fin_arr