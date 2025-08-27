# Given an integer array nums and an integer k, return the kth largest element in the array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        target = len(nums_sorted) - k

        return nums_sorted[target] 

        