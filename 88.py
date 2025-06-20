def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_list = []
        left = 0
        right = 0
        while True:
            if left == m:
                new_list.extend(nums2[right:])
                break
            if right == n:
                new_list.extend(nums1[left:])
                break
            if nums1[left] < nums2[right]:
                new_list.append(nums1[left])
                left += 1 
            else: 
                new_list.append(nums2[right])
                right += 1
        for i in range(m + n):
            nums1[i] = new_list[i]