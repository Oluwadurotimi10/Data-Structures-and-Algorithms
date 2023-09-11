# Leetcode 1244

class Leaderboard:
    '''
    - Initialize scores dictionary to track player and scores <playerId, score>
    - add score: if player not in scores, add to scores with value 0, add += scores to playerId
    - top: Init empty heap, for K values, keep adding values from scores.values() to heap whilst also checking if len(heap) > K         (if it is pop from heap). Eventually len(heap) == K

    '''

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0
        self.board[playerId] += score

    def top(self, K: int) -> int:
        top_k = []
        summ = 0

        for scores in self.board.values():
            heapq.heappush(top_k, scores)

            if len(top_k) > K:
                heapq.heappop(top_k)

        while top_k:
            summ += heapq.heappop(top_k)

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0

