""""
    Leetcode: Number of students unable to eat lunch (1700)
"""

def countStudents(students, sandwiches) -> int:


    while students:
        if students[0] != sandwiches[0]:
            front = students.pop(0)
            students.append(front)
        else:
            students.pop(0)
            sandwiches.pop(0)

        if len(sandwiches) > 0:
            if sandwiches[0] not in students:
                break

    if students:
        return len(students)
    return 0
