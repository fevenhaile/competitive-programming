class FrequencyTracker:
    def __init__(self):
        self.frequency_count = defaultdict(int)
        self.frequency_tracker = defaultdict(int)

    def add(self, number: int) -> None:
        current_frequency = self.frequency_count[number]
        self.frequency_tracker[current_frequency] -= 1
        self.frequency_count[number] += 1
        updated_frequency = self.frequency_count[number]
        self.frequency_tracker[updated_frequency] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.frequency_count:
            current_frequency = self.frequency_count[number]
            self.frequency_tracker[current_frequency] -= 1
            if self.frequency_tracker[current_frequency] == 0:
                del self.frequency_tracker[current_frequency]
            self.frequency_count[number] -= 1
            if self.frequency_count[number] > 0:
                updated_frequency = self.frequency_count[number]
                self.frequency_tracker[updated_frequency] += 1
            else:
                del self.frequency_count[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frequency_tracker and self.frequency_tracker[frequency] > 0