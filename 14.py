def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = lambda word: len(word))
        outputStr = ""okay 
        compare = strs[0]
        for letter in compare:
            for word in strs[1:]:
                if word[len(outputStr)] != letter:
                    return outputStr
            outputStr += letter
        return outputStr