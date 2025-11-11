class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0

        for i in range(k):
            if blocks[i] == "W":
                white_count += 1
        
        min_operations = white_count

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove the leftmost character from window
            if blocks[i - k] == "W":
                white_count -= 1
            
            # Add new character to the window
            if blocks[i] == "W":
                white_count += 1
            
            min_operations = min(min_operations, white_count)
        
        return min_operations

