# Leetcode 359

# using hashmap
# TC: O(log(1)), SC:O(log(N))
class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not timestamp and not message:
            return None
        if self.logs.get(message, 0) > timestamp:
            return False
        self.logs[message] = timestamp + 10
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# using queue and set
# TC: Constructor: O(1), shouldPrintMessage(timestamp: int, message: str): O(n), SC:O(log(N))

class Logger:

    def __init__(self):
        self.messageQueue = deque()
        self.messageSet = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while self.messageQueue:
            # remove messages that are 10 secs from the current timestamp
            topTimestamp, topMessage = self.messageQueue[0]

            if timestamp < topTimestamp + 10:
                break
            self.messageQueue.popleft()
            self.messageSet.remove(topMessage)

        if message in self.messageSet:
            return False

        self.messageQueue.append((timestamp, message))
        self.messageSet.add(message)
        return True