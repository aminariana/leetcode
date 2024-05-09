from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    w = len(nums1)
    m -= 1
    n -= 1
    while m >= 0 or n >= 0:
        w -= 1
        if m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[w] = nums1[m]
                m -= 1
            else:
                nums1[w] = nums2[n]
                n -= 1
        elif m >= 0:
            nums1[w] = nums1[m]
            m -= 1
        elif n >= 0:
            nums1[w] = nums2[n]
            n -= 1
    # print(nums1)
