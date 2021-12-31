# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:46:13 2020

@author: JADESOLA
"""
obj = {
       "num":1,
       "test":[],
       "data":{
               "val":4,
               "info":{
                       "isRight":True,
                       "random":44,
                      }
              }
        }
def stringifyNumbers(obj):
    """
        This function takes in an object and finds all the values which are numbers and converts
        them to string.
    """
    for item in obj:
        if type(obj[item]) is int:
            obj[item] = str(obj[item])
        elif type(obj[item]) is dict:
            stringifyNumbers(obj[item])
    return obj
print(stringifyNumbers(obj))