class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        prefixes={}
        prefixes[-1]={}
        n = len(word)
        l=0
        total = 0
        for i in range(n):
            if abs(ord(word[i])-ord(word[i-1] if i>0 else word[i]))>2:
                prefixes={}
                prefixes[i-1]={}
                l=i
            prefixes[i]=prefixes[i-1].copy()
            if word[i] not in prefixes[i]:
                prefixes[i][word[i]] = 0
            prefixes[i][word[i]] += 1
            for j in range(1,27):
                left=i-k*j
                if left<l-1:
                    break
                check = True
                left_prefixes = prefixes.get(left, {})
                right_prefixes = prefixes[i]

                # Track number of distinct characters
                distinct_chars = 0

                for key in right_prefixes:
                    left_count = left_prefixes.get(key, 0)
                    diff = right_prefixes[key] - left_count
                    if diff not in (0, k):
                        check = False
                        break
                    if diff == k:
                        distinct_chars += 1

                # The substring must have exactly j characters with count = k
                if check and distinct_chars == j:
                    total += 1
        return total


