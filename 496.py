def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []
        for number in nums1:
            if nums2.index(number) < len(nums2) - 1 :
                for elem in nums2[nums2.index(number):]:
                    if elem > number:
                        final.append(elem)
                        break
                else:
                    final.append(-1)
            else:
                final.append(-1)
        return final

# better solution:
# def nextGreaterElement(self, nums1, nums2):
#         stack = []
#         d = {}
#         for n in nums2:
#             while stack and n > stack[-1]:
#                 d[stack.pop()] = n
#             stack.append(n)
#         for n in stack:
#             d[n] = -1
#         return [d[x] for x in nums1]