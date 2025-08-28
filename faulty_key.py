class Solution:
    def finalString(self, s: str) -> str:
        # monitor order of characters and add them
        result = []

        for character in s:
            if character == "i":
                result.reverse()
            
            else:
                result.append(character)
        return "".join(result)
        