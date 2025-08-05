class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = s.split()

        
        return len(answer[len(answer) - 1])