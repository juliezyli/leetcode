def reverseOnlyLetters(self, s: str) -> str:
        lst = list(s)
        left = 0
        right = len(lst) - 1 
        while left < right:
            if lst[left].isalpha() and lst[right].isalpha():
                temp = lst[left]
                lst[left] = lst[right]
                lst[right] = temp 
                left += 1 
                right -= 1 
            else:
                if not lst[left].isalpha():
                    left += 1
                if not lst[right].isalpha():
                    right -= 1
        return ''.join(lst)