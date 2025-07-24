def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        lst = list(s)
        left = 0 
        right = len(lst) - 1
        while left < right: 
            if lst[left] in vowels and lst[right] in vowels: 
                temp = lst[left]
                lst[left] = lst[right]
                lst[right] = temp
                left += 1
                right -= 1 
            if lst[left] not in vowels:
                    left += 1 
            if lst[right] not in vowels:
                    right -= 1
        return ''.join(lst)