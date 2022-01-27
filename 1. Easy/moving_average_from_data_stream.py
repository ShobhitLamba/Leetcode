class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.currlen = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.currlen += 1
        if len(self.window) > self.size:
            return sum(self.window[self.currlen - self.size:]) / self.size
        else:
            return sum(self.window) / self.currlen


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
