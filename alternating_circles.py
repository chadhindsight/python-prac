class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # we need to check that colors[i] != colors[i + 1] and. colors[i + 1] != colors[i + 2]
        n = len(colors)
        count = 0

        for i in range(n):
            if (colors[i] != colors[(i + 1) % n] and colors[(i + 1 ) % n] != colors[(i + 2) % n]):
                count += 1
        
        return count