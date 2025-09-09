class Solution:
    def findTheDifference(self, s: str, t: str) -> str
        val1 = {}
        val2 = {}

        for word in s:
            val1[word] = val1.get(word, 0) + 1
        
        for word in t:
            val2[word] = val2.get(word, 0) + 1
        
        for val in val2:
            if val1.get(val, 0) != val2[val]:
                return val