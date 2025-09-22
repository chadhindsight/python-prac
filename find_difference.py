class Solution:
    def findTheDifference(self, s: str, g: str) -> str:
        val1 = {}
        val2 = {}

        for word in s:
            val1[word] = val1.get(word, 0) + 1
        
        for word in g:
            val2[word] = val2.get(word, 0) + 1
        
        for value in val2:
            if val1.get(value, 0) != val2[value]:
                return value