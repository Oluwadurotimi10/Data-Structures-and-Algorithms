# Leetcode 381

def __init__(self):
    self.collection = defaultdict(set)
    self.vals = []
    self.idx = 0


def insert(self, val: int) -> bool:
    in_collection = False

    if not self.collection[val]:
        in_collection = True

    self.collection[val].add(self.idx)
    self.vals.append(val)
    self.idx += 1

    return in_collection


def remove(self, val: int) -> bool:
    if not self.collection[val]:
        return False

    idx_remove = self.collection[val].pop()
    last_val = self.vals[-1]
    self.vals[idx_remove] = last_val
    self.collection[last_val].add(idx_remove)
    self.collection[last_val].remove(self.idx - 1)

    self.vals.pop()
    self.idx -= 1
    return True


def getRandom(self) -> int:
    return random.choice(self.vals)