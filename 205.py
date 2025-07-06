# the map function maps a function onto an iterable
    # index finds the first instance of a string 
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]