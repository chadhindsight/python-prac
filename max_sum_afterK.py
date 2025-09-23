def largestSumAfterKNegations(nums , k) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1:
            min_val = min(nums)
            return sum(nums) - 2 * min_val
        
        return sum(nums)  