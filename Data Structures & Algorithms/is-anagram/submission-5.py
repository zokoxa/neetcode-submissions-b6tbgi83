class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else :
            s_copy = s
            for letter in s:
                s_copy = s_copy.replace(letter, "", 1)
                t = t.replace(letter, "", 1)

        return len(s_copy) == len(t)
