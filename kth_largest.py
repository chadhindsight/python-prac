class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        target = len(nums_sorted) - k

        return nums_sorted[target] 

        