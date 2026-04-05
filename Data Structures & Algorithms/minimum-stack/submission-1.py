class MinStack:
    ElementWithCachedMin = collections.namedtuple('ElementWithCachedMin', 
    ('element', 'min'))


    def __init__(self):
        self._element_with_cached_min = []
        

    def push(self, val: int) -> None:
        self._element_with_cached_min.append(
            self.ElementWithCachedMin(val, val if not self._element_with_cached_min else
            min(val,self.getMin()))
        )

    def pop(self) -> None:
        self._element_with_cached_min.pop()

    def top(self) -> int:
        return self._element_with_cached_min[-1].element

    def getMin(self) -> int:
        return self._element_with_cached_min[-1].min
