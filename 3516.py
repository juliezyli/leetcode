def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)
        dist2 = abs(y - z)
        if dist2 > dist1:
            return 1
        if dist1 > dist2:
            return 2
        else:
            return 0