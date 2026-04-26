class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n

        num1, num2 = 0, 0
        diff_bit = xor_all & -xor_all  # rightmost set bit

        for n in nums:
            if n & diff_bit:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]