class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + word + '/0'
        
        return res


    def decode(self, s: str) -> List[str]:
        ss = s.split('/0')
        return ss[0:len(ss)-1:]
