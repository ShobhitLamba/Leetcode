class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n_dict, stack, ans = {}, [], []

        for x in nums2:
            while len(stack) and stack[-1] < x:
                n_dict[stack.pop()] = x
            stack.append(x)

        for x in nums1:
            ans.append(n_dict.get(x, -1))

        return ans
