class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      result_str = ""
      i = j = 0

      while i < len(word1) and j < len(word2):
        result_str += word1[i]
        result_str += word2[j]
        i += 1
        j += 1

      result_str += word1[i:]
      result_str += word2[j:]
      return result_str
