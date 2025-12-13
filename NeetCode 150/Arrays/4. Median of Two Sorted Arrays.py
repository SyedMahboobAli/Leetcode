class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        # This ensures O(log(min(m, n))) time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # m = length of smaller array
        # n = length of larger array
        m, n = len(nums1), len(nums2)

        # Number of elements that must be on the LEFT side
        # +1 helps when total length is odd
        total_left = (m + n + 1) // 2

        # Binary search boundaries on nums1
        l, r = 0, m # this is to compute mid partition not index. so using m and not m-1

        while l <= r: # This is BS

            # mid1 → partition index in nums1
            mid1 = (l + r) // 2

            # mid2 → partition index in nums2
            # Ensures left side has total_left elements
            mid2 = total_left - mid1

            # Left side max element of nums1
            # If mid1 == 0 → nothing on left → use -infinity
            left1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")

            # Right side min element of nums1
            # If mid1 == m → nothing on right → use +infinity
            right1 = nums1[mid1] if mid1 < m else float("inf")

            # Left side max element of nums2
            left2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")

            # Right side min element of nums2
            right2 = nums2[mid2] if mid2 < n else float("inf")

            # Valid partition condition
            # All left-side elements <= all right-side elements
            if left1 <= right2 and left2 <= right1:

                # Odd total length → median is max of left elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length → average of two middle elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # If left1 is too large, move partition left
            elif left1 > right2:
                r = mid1 - 1

            # If left2 is too large, move partition right
            else:
                l = mid1 + 1

'''
Only code:
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1

m, n = len(nums1), len(nums2)
total_left = (m + n + 1) // 2

l, r = 0, m

while l <= r:
    mid1 = (l + r) // 2
    mid2 = total_left - mid1

    left1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
    right1 = nums1[mid1] if mid1 < m else float("inf")

    left2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
    right2 = nums2[mid2] if mid2 < n else float("inf")

    if left1 <= right2 and left2 <= right1:
        if (m + n) % 2 == 1:
            return max(left1, left2)
        return (max(left1, left2) + min(right1, right2)) / 2

    elif left1 > right2:
        r = mid1 - 1
    else:
        l = mid1 + 1
'''
