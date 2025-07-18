def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1, 2, 4, 8]
        mins = [1, 2, 4, 8, 16, 32]
        if turnedOn < 0 or turnedOn > 10:
            return []
        final = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn: 
                    final.append("{}:{:02d}".format(hour, minute)) # a way of formatting where 0 means pad with 0, 2 means there are two digits, and d means that it is a decimal
        return final