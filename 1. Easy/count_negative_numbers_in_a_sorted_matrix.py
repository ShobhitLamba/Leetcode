class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.binarySearch(array) for array in grid])

    def binarySearch(self, arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < 0:
                end = mid - 1
            else:
                start = mid + 1

        return len(arr) - start
