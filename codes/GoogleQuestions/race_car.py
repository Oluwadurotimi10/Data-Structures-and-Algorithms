import collections

def racecar( target: int) -> int:
    queue = collections.deque()
    visited = set()

    queue.append([0, 1, 0])

    while queue:
        position, speed, moves = queue.popleft()

        if position == target:
            return moves

        if (position, speed) not in visited:
            visited.add((position, speed))
            queue.append([position + speed, speed * 2, moves + 1])

            if ((position + speed) > target and speed > 0) or ((position + speed) < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append([position, speed, moves + 1])
            print(queue)
print(racecar(6))