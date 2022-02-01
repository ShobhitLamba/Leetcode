class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        op, extra = [], []

        for elem in arr2:
            op.extend([elem] * count[elem])

        for elem in set(arr1) - set(arr2):
            extra.extend([elem] * count[elem])

        return op + sorted(extra)
