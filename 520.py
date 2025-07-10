def detectCapitalUse(self, word: str) -> bool:
        word_list = list(word)
        if word.isupper():
            return True
        if any(x.isupper() for x in word_list[1:]):
            return False
        return True