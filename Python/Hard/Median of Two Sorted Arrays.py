class Solution:
    def findKth(self, k, nums1, nums2):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        len1, len2 = len(nums1), len(nums2)
        idx1, idx2 = len1 // 2, len2 // 2
        mid1, mid2 = nums1[idx1], nums2[idx2]

        if idx1 + idx2 < k:
            if mid1 > mid2:
                return self.findKth(k - idx2 - 1, nums1, nums2[idx2 + 1:])
            else:
                return self.findKth(k - idx1 - 1, nums1[idx1 + 1:], nums2)
        else:
            if mid1 > mid2:
                return self.findKth(k, nums1[:idx1], nums2)
            else:
                return self.findKth(k, nums1, nums2[:idx2])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            return (self.findKth(total_length // 2, nums1, nums2) + self.findKth(total_length // 2 - 1, nums1, nums2)) / 2
        else:
            return self.findKth(total_length // 2, nums1, nums2)
