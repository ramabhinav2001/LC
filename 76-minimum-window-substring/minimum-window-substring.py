class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        s1_cnt = {}
        s2_cnt = {}

        ans = ""
        min_len = float('inf')

        start = 0

        if n > m:
            return ""

        for i in range(n):
            s2_cnt[t[i]] = s2_cnt.get(t[i], 0) + 1

        have = 0
        need = len(s2_cnt)

        for end in range(m):

            s1_cnt[s[end]] = s1_cnt.get(s[end], 0) + 1

            if s[end] in s2_cnt and s1_cnt[s[end]] == s2_cnt[s[end]]:
                have += 1

            while have == need:

                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    ans = s[start:end + 1]

                s1_cnt[s[start]] -= 1

                if s[start] in s2_cnt and s1_cnt[s[start]] < s2_cnt[s[start]]:
                    have -= 1

                start += 1

        return ans