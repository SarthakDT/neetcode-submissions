class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr = ""
        for istr in strs:
            enstr += str(len(istr)) + '#' + istr
        return enstr

    def decode(self, s: str) -> List[str]:
        i = 0
        destr = []
        while i < len(s):
            length = 0
            while s[i]!="#":
                length=length*10+int(s[i])
                i+=1

            i+=1

            destr.append(s[i:i+length])

            i+=length

        return destr


            