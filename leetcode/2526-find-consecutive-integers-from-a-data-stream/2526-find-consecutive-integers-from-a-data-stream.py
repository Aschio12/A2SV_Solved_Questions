class DataStream:
    def __init__(self, value: int, k: int):
        self.target = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        if num == self.target:
            self.streak += 1
        else:
            self.streak = 0
        
        return self.streak >= self.k