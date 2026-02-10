class FrequencyTracker:

    def __init__(self):
        self.count_num=defaultdict(int)
        self.freq=defaultdict(int)

    def add(self, number: int) -> None:

        if number in self.count_num:
            old_count=self.count_num[number]
            self.freq[old_count]-=1

            if self.freq[old_count]==0:
                del self.freq[old_count]

        self.count_num[number]+=1
        self.freq[self.count_num[number]]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.count_num:

            old=self.count_num[number]
            self.freq[old]-=1

            if self.freq[old]==0:
                del self.freq[old]

            self.count_num[number]-=1
            if self.count_num[number]>0:
                self.freq[self.count_num[number]]+=1
            else:
                del self.count_num[number]

            if self.count_num[number]==0:
                del self.count_num[number]

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)