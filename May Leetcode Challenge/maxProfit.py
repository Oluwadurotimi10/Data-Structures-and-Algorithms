# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:23:15 2021

@author: JADESOLA
"""

def maxProfit(k, profit):
    # Write your code here
    max_profit = 0
    sum_profit = 0
    if len(profit) == 2:
        return (sum(profit))
    if (len(profit) / k) == 2:
        return (max(sum(profit[:k]), sum(profit[k:])))
    i = 0
    j = k
    adj_diff = len(profit) // 2
    while i < len(profit):
        idx_i =i+adj_diff
        idx_j =j+adj_diff
        if j <= adj_diff:
            sum_profit = sum(profit[:j]) + sum(profit[idx_i:idx_j]) 
        else:
            over_diff = j - adj_diff
            sum_profit = sum(profit[:j]) + sum(profit[idx_i:]) + sum(profit[:over_diff])
        max_profit = max(max_profit, sum_profit) 
        i += 1
        j += 1
    return max_profit