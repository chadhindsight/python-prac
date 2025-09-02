# reverse only the letters of a string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        str_list = list(s)
        i = 0
        j = len(str_list) - 1

        while i < j:
            if str_list[i].isalpha() and str_list[j].isalpha():
                str_list[i], str_list[j] = str_list[j], str_list[i]
                i += 1
                j -= 1
            
            elif not str_list[i].isalpha():
                i +=1
            elif not str_list[j].isalpha():
                j -= 1
        
        return ''.join(str_list)
        