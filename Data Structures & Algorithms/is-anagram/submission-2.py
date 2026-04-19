class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if tmp.get(s[i], None) is None:
                tmp[s[i]] = 1
            else:
                tmp[s[i]] += 1
        count = 0
        for i in range(len(t)):
            if tmp.get(t[i], None) is None:
                return False
            tmp[t[i]] -= 1
            if tmp[t[i]] < 0:
                return False
        #     count += 1
        # print(f"Count : {count}")
        # if count != len(s):
        #     return False
        return True
            