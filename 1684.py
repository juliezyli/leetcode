def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = list(allowed) 
        count = 0
        for word in words:
            word = list(word)
            if set(allowed).issubset(set(word)) or set(word).issubset(set(allowed)):
                count += 1
                for letter in word:
                    if letter not in allowed:
                        count -= 1
        return count