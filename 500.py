def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        final = []
        for word in words:
            word2 = word.lower()
            word_list = list(word2)
            if set(word_list).issubset(set(row1)) or set(word_list).issubset(set(row2)) or set(word_list).issubset(set(row3)):
                final.append(word)
        return final