class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        ans = []

        for k in nums1.keys():
            if k in nums2.keys():
                ans.extend([k] * min(nums1[k], nums2[k]))

        return ans
