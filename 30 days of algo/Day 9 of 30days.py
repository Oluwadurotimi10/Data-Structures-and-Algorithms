# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:05:11 2020

@author: JADESOLA
"""
"""
Given a paragraph and a list of words, return the most frequent word
"""

def most_occurence(words):
    word_list = words.split(' ')
    frequency_map = {}
    for word in word_list:
        word = str.lower(word)
        frequency_map[word] = frequency_map.get(word,0)+1
        
    max_so_far = frequency_map[str.lower(word_list[0])]
    word = str.lower(word_list[0])
    for j in frequency_map:
        if frequency_map[j] > max_so_far:
            max_so_far = frequency_map[j]
            word = j
        elif frequency_map[j] <= max_so_far:
            continue
    return word        
#words = 'Bob hit a ball the hit, BALL flew far after it was hit'
words = "hey cow brown cow"
print(most_occurence(words))
        