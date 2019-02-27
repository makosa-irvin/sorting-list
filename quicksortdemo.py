# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:28:25 2019

@author: User
"""

from random import randrange, shuffle 
def quicksort(list, start, end):
  # this portion of listay has been sorted
  if start >= end:
    return list

  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print(pivot_element)

  # swap random element with last element in sub-listay
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  # Call quicksort on the "left" and "right" sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer +1,end)
  return list
  
unsorted_list = [31,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!
lst = quicksort(unsorted_list,0,len(unsorted_list)-1)
print(lst)