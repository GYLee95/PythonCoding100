# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:29:40 2025

@author: gangylee

@Description: 
    - Exercise 10 - Sequence Item Picking

        Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
        
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        Expected output: 
        
        ['a', 'c', 'e', 'g', 'i'] 
    
"""

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(letters[::2])


'''
Explanation: 

The complete syntax of list slicing is [start:end:step] . 
When you don't pass a step, Python assumes the step is 1. [:]  itself means to get everything from start to end. 
So, [::2]  means get everything from start to end at a step of two.
'''