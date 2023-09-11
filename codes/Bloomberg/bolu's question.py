import heapq

class Trade:
    def __init__(self):
        # creating a stack to store trade
        self.stock = []
        # creating a minheap to keep track of minimum order
        self.heap = []


    def add0rder(self, amount):
        self.stock.append(amount)
        heapq.heappush(self.heap, amount)

    def executeOrder(self):
        latest_order = self.stock.pop()
        if latest_order == self.heap[0]:
            heapq.heappop(self.heap)
        return latest_order

    def extractMinOrder(self):
        return self.heap[0]


if __name__ == '__main__':
    trade = Trade()
    trade.add0rder(100)
    trade.add0rder(200)
    trade.add0rder(50)
    trade.add0rder(40)
    print(trade.executeOrder())
    print(trade.extractMinOrder())


    def __init__(self):
        self.scores = {}


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score


    def top(self, K: int) -> int:
        heap = []

        heapq.heapify(heap)

        for value in self.scores.values():
            heapq.heappush(heap, value)

            if len(heap) > K:
                heapq.heappop(heap)
        res = 0

        while heap:
            res += ((heapq.heappop(heap)))

        return res
        # heap = []

        # heapq.heapify(heap)

        # for value in self.scores.values():
        #     heapq.heappush(heap, value)

        #     if len(heap) > K:
        #         heapq.heappop(heap)

        # res = 0

        # while heap:
        #     res += (heapq.heappop(heap))
        #     # K -= 1

        # return res


    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


