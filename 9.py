def isPalindrome(self, x: int) -> bool:
        final = True
        newList = list(str(x))
        i = 1
        for number in newList[:int(len(newList) / 2)]:
            if number != newList[len(newList) - i]:
                final = False
            i += 1
        return final