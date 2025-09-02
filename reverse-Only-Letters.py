# reverse only the letters of a string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        str_list = list(s)
        left = 0
        right = len(str_list) - 1

        while left < right:
            if str_list[left].isalpha() and str_list[right].isalpha():
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1
            
            elif not str_list[left].isalpha():
                left +=1
            elif not str_list[right].isalpha():
                right -= 1
        
        return ''.join(str_list)
        