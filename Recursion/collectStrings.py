# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:44:46 2020

@author: JADESOLA
"""
obj = {
       "stuff":'foo',
       "data":{
       "val":{
       "thing":{
               "info":'bar',
               "moreInfo":{
                       "evenMoreInfo":{
                               "weMadeIt":'baz',
                               }}}}}}


def collectStrings(obj):
    """
        This function accepts an object and returns an array of all the values in the object of 
        string type.
    """
    arr =[]
    for item in obj:
        if type(obj[item]) is str:
            arr.append(obj[item])
        elif type(obj[item]) is dict:
            arr = arr + collectStrings(obj[item])
    return arr
print(collectStrings(obj))   