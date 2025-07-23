import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[^a-zA-Z0-9\s]', '', s) #removes everything that is not space/alphanumeric
        final = new.replace(" ", "")
        if not final:
            return True
        newList = list(final.lower())
        state = True
        i = 1
        for element in newList[:int(len(newList) / 2)]:
            if element != newList[len(newList) - i]:
                state = False
            i += 1
        return state