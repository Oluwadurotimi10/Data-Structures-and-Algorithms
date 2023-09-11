# Leetcode 380
# TC: O(1) for all operations
# SC : O(n)
class RandomizedSet:

    def __init__(self):
        self.set_map = {}
        self.val_list = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        if val in self.set_map:
            return False
        self.set_map[val] = self.idx
        self.val_list.append(val)
        self.idx += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set_map:
            return False

        idx_remove = self.set_map[val]
        self.set_map[self.val_list[-1]] = idx_remove
        self.val_list[idx_remove], self.val_list[-1] = self.val_list[-1], self.val_list[idx_remove]
        self.idx -= 1
        self.val_list.pop()
        self.set_map.pop(val)
        return True

    def getRandom(self) -> int:

        rand_idx = randint(0, len(self.val_list) - 1)
        return self.val_list[rand_idx]
        # or random.choice(self.vals)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()