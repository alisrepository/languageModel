# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:54:51 2019

@author: ALI
"""

import itertools # HELPS TO CONVERT MULTIDIMENTIONAL LIST TO SINGLE
def get_prob(total_wordA, total_wordB, total_words):
    prob_wordA = (total_wordA/total_words)
    prob_wordB = (total_wordB/total_words)
    prob = prob_wordA * prob_wordA * prob_wordB
    return prob

def find_word_get_freq(list1, var):
    temp_holder = 0
    idx = 0
    while(idx < len(list_of_word_count)):
        if(var == list_of_word_count[idx]):
            temp_holder = list_of_word_count[idx+1]
            break
        idx += 1
    return temp_holder

def get_total_words(list1):
    
    indx = 0
    temp = 0
    while(indx < len(list_of_word_count)):
        if(str(type(list_of_word_count[indx])) != "<class 'str'>"):
            temp += list_of_word_count[indx]
        indx += 1
    return temp

list_of_queries = ["why are you here","how to create web page","how to make beautiful web page","why we learn maths in ml","why we learn maths in machine learning","create beautiful web page","create beautiful web page"]

list_of_queried_word = []
for sentence in list_of_queries:
    list_of_queried_word.append(sentence.split())#THIS MAKES LISTS INSIDE LIST WHICH IS PROBLEM FOR ME
    
list_of_queried_words = list(itertools.chain(*list_of_queried_word))


list_of_unique_words = list(set(list_of_queried_words))

list_of_word_count = []
for word in list_of_unique_words:
    count = list_of_queried_words.count(word)
    list_of_word_count.append(word)
    list_of_word_count.append(count)

#if(str(type(1)) == "<class 'str'>"):
#    print("string")
total_words = get_total_words(list_of_word_count)
print(total_words)
var = "why"
var_freq_holder = find_word_get_freq(list_of_word_count, var)

list_word_prob = []
index = 0
while(index < len(list_of_word_count)):
    if(var == list_of_word_count[index] or str(type(list_of_word_count[index])) != "<class 'str'>"):
        22
    else:
        list_word_prob.append(list_of_word_count[index])
        list_word_prob.append(get_prob(list_of_word_count[index+1], var_freq_holder, total_words))
        
    index += 1

print(list_word_prob)    
