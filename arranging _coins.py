class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            coinsNeeded = mid * (mid + 1) // 2

            if coinsNeeded == n:
                return mid
            elif coinsNeeded < n:
                low = mid + 1
            elif coinsNeeded > n:
                high = mid -1

        return high