def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pivot = nums[0]
        # leftPointer = -1
        # rightPointer = len(nums)
        # while True:
        #     while True:
        #         leftPointer += 1
        #         if nums[leftPointer] >= pivot:
        #             break 
        #     while True:
        #         rightPointer -= 1 
        #         if nums[rightPointer] <= pivot: 
        #             break
        #     if leftPointer > rightPointer:
        #         break 
        #     nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1