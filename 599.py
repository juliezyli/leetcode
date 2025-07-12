def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        for word in list1:
            if word in list2:
                common.append(word)
        least = list1.index(common[0]) + list2.index(common[0])
        final = []
        for word in common:
            if list1.index(word) + list2.index(word) == least:
                final.append(word)
            else:
                if list1.index(word) + list2.index(word) < least:
                    final = [word]
                    least = list1.index(word) + list2.index(word)
        return final