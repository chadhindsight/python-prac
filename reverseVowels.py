class Solution:
    def reverseVowels(self, s: str) -> str:
        # hash for reference to check vowels. O(1) lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        str_list = list(s)
        i = 0
        j = len(str_list) - 1

        while i < j:
            if str_list[i].lower() in vowels and str_list[j].lower() in vowels:
                str_list[i], str_list[j] = str_list[j], str_list[i]
                j -= 1
                i += 1

            elif str_list[i].lower() not in vowels:
                i+= 1
            elif str_list[j].lower() not in vowels:
                j -= 1
        
        return ''.join(str_list)