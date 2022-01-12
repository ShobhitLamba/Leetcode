class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transformStr(s):
            index_map = {}
            new_str = []

            for i, c in enumerate(s):
                if c not in index_map:
                    index_map[c] = i
                new_str.append(str(index_map[c]))

            return " ".join(new_str)

        return transformStr(s) == transformStr(t)
                
