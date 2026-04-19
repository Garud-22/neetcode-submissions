class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_list = []

        for s in strs:
            encoded_list.append(str(len(s)) + "#" + s)

        encoded_str = "".join(encoded_list)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
