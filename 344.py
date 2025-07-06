def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            left = i
            right = len(s) - 1 - i
            if left > right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp