# Leetcode 2034

# TC: O(K log K)  SC: O(N) where N is number of distinct timestamps
class StockPrice:

    def __init__(self):
        self.stock_map = {}
        self.curr = -1

        self.heapmax = []
        self.heapmin = []

    # TC: O(log k) due to inserting into a heap
    def update(self, timestamp: int, price: int) -> None:
        self.curr = max(self.curr, timestamp)

        self.stock_map[timestamp] = price

        heappush(self.heapmax, (-price, timestamp))
        heappush(self.heapmin, (price, timestamp))

    # TC: O(1) due to inserting into a heap
    def current(self) -> int:
        return self.stock_map[self.curr]

    # TC: O(K log K) where K is no of elements in heap
    def maximum(self) -> int:

        currP, currT = heappop(self.heapmax)

        while -currP != self.stock_map[currT]:
            currP, currT = heappop(self.heapmax)

        heappush(self.heapmax, (currP, currT))
        return -currP

    # TC: O(K log K) where K is no of elements in heap
    def minimum(self) -> int:
        currP, currT = heappop(self.heapmin)

        while currP != self.stock_map[currT]:
            currP, currT = heappop(self.heapmin)

        heappush(self.heapmin, (currP, currT))
        return currP