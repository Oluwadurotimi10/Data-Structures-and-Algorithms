def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    course_map = {i: [] for i in range(numCourses)}
    visited = set()

    for a, b in prerequisites:
        course_map[a].append(b)

    def dfs(a):
        if a in visited:
            return False
        if course_map[a] == []:
            return True
        visited.add(a)
        for i in course_map[a]:
            if not dfs(i):
                return False
        visited.remove(a)
        course_map[a] = []
        return True

    for course in course_map:
        if not dfs(course):
            return False
    return True

