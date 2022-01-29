class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_list = [v for v in Counter(arr).values()]

        return len(set(count_list)) == len(count_list)
