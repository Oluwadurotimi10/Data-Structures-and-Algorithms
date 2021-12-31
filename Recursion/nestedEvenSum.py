# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:09:46 2020

@author: JADESOLA
"""


obj1 = {
  "outer": 2,
  "obj": {
    "inner": 4,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


def nestedEvenSum(obj1,summ=0):
    """
        This function accepts an object and returns the sum of all even numbers
        with the object which may contain nested objects.
    """
    for item in obj1:
        if (type(obj1[item]) is int) and (obj1[item]%2 == 0) :
            summ += obj1[item]
            
        elif type(obj1[item]) is dict:
            summ += nestedEvenSum(obj1[item])
    return summ

print(nestedEvenSum(obj1,summ=0))
