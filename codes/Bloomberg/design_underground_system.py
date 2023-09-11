# Leetcode 1396
# TC :O(1), SC: O(|passengers| + |stations|^2)

class UndergroundSystem:

    def __init__(self):
        self.checkIn_map = {}
        self.paths = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_stn, time = self.checkIn_map.pop(id)
        path = start_stn + '->' + stationName
        if path not in self.paths:
            self.paths[path] = [0, 0]
        self.paths[path][0] += 1
        self.paths[path][1] += t - time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path = startStation + '->' + endStation
        return self.paths[path][1] / self.paths[path][0]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)