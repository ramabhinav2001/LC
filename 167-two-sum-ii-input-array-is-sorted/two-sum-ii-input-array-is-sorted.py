class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashm={}
        sub=0
        for i in range(len(numbers)):
            sub=target-numbers[i]
            if sub in hashm:
                return [hashm[sub]+1,i+1]
            hashm[numbers[i]]=i
        return []
