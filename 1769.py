def minOperations(self, boxes: str) -> List[int]:
        ans = []
        boxes_list = list(boxes)
        for i in range(len(boxes_list)):
            number = 0
            for j in range(len(boxes_list)):
                if boxes_list[j] == '1':
                    number += abs(i - j)
            ans.append(number)
        return ans