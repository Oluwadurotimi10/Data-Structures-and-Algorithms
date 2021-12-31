# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:43:41 2021

@author: JADESOLA
"""
import heapq
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
def scheduleCourse(courses):
    """
    There are n different online courses numbered from 1 to n. You are given an
    array courses where courses[i] = [durationi, lastDayi] indicate that the ith
    course should be taken continuously for durationi days and must be finished 
    before or on lastDayi.
    
    You will start on the 1st day and you cannot take two or more courses 
    simultaneously.

    Return the maximum number of courses that you can take.
    """
    
    heap = []
    total = 0
    for duration, last in sorted(courses, key=lambda val:val[1]):
        if duration + total <= last:
            total += duration
            heapq.heappush(heap, -duration)
        elif heap and -heap[0] > duration:
            total += duration + heapq.heappop(heap)
            print(heapq.heappop(heap))
            heapq.heappush(heap, -duration)
    return len(heap)
print(scheduleCourse(courses))