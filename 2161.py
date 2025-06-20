def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        returnList = []
        for number in nums:
            if number < pivot:
                returnList.append(number)
        for number in nums:
            if number == pivot:
                returnList.append(number)
        for number in nums:
            if number > pivot:
                returnList.append(number)
        return returnList