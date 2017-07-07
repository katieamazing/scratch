
class Reservoir:
    def __init__(self, size):
        self.size = size
        self.pool = []
        self.count = 0

    def try_to_add(self, new_sample):
        if self.should_sample():
            if len(self.pool) < self.size:
                self.pool.append(new_sample)
            else:
                self.pool[random(0, self.size)] = new_sample
        self.count += 1

    def should_sample(self):
        return random(0, 1) < self.size/self.count
