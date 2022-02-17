class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # build a filter based on the first word
        w = words[0]
        d = Counter(w)

        for s in words:
            ds = Counter(s)
            del_list = []
            for k in d.keys():
                if not k in ds.keys():
                    del_list.append(k)

            # 1. remove all the difference (d.keys - d intersect ds)
            for dl in del_list:
                del d[dl]

            # 2. update the existing letter's frequency
            for k, v in ds.items():
                if k in d.keys() and ds[k] <= d[k]:
                    d[k] = ds[k]

        ans = []

        # populate ans from the original filter
        for k, v in d.items():
            for _ in range(v):
                ans.append(k)

        return ans 
