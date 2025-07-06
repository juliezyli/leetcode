def scoreOfString(self, s: str) -> int:
        char = list(s)
        score = 0
        for i in range(len(char) - 1):
            score += abs(ord(s[i + 1]) - ord(s[i]))
        return score