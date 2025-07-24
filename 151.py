def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst = s.split()
        left = 0
        right = len(lst) - 1
        while left < right:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp 
            left += 1 
            right -= 1
        return " ".join(lst)