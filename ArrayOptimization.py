import timeit
import inspect
import time
import types
from typing import cast

#The task is to find if the two separate arrays have common items and return true if this is the case. Else return false.


def slowFunction(array1, array2):
  

  for item in array1:
    for val in array2:
      if item == val:
        print("found "+ val)
        return True

  return False

def fasterFunction(array1, array2):

# remove duplicates from both arrays by making the list a dict
  array1_singles = list(dict.fromkeys(array1)) 
  array2_singles = list(dict.fromkeys(array2))

  for item in array1_singles:
    for val in array2_singles:
      if item == val:
        print("found "+ val)
        return True

  return False

def fasterFunctionSorted(array1, array2):

# remove duplicates from both arrays by making the list a dict
  array1_singles = list(dict.fromkeys(array1)) 
  array2_singles = list(dict.fromkeys(array2)) 

  array1_singles.sort()
  array2_singles.sort()

  for item in array1_singles:
    for val in array2_singles:
      if item == val:
        print("found "+ val)
        return True

  return False

def anotherFunction(array1, array2):

  #remove duplicates from both arrays
  array1_singles = list(dict.fromkeys(array1)) 
  array2_singles = list(dict.fromkeys(array2))


  #give letters numerical representations
  array1_as_numerical = []
  array2_as_numerical = []

  for character in array1_singles:
      number = ord(character) - 96
      array1_as_numerical.append(number)

  for character in array2_singles:
      number = ord(character) - 96
      array2_as_numerical.append(number)

  #sort the array ascending
  array1_as_numerical.sort()
  array2_as_numerical.sort()

  for item in array1_as_numerical:
    for target in array2_as_numerical:
      if target > item:
        break
      elif target < item:
        continue
      else:
        print("found item")
        return True

  return False


#iterate through the lists in reverse and pop the item after no match
def reversePopFunction(array1, array2):
# remove duplicates from both arrays by making the list a dict
  array1_singles = list(dict.fromkeys(array1)) #convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates
  array2_singles = list(dict.fromkeys(array2)) #convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates

  array1_singles.sort()
  array2_singles.sort(reverse = True)

  for item in reversed(array1_singles):
    for val in array2_singles:
      if item == val:
        print("found "+ val)
        return True
    array1_singles.pop()
  return False

#proposed solution is create an object of array1 and check if object contains array2 items, so moving from O(a^2) to O(a)

def timed_code(input_size, func):
  array1 = []
  array2 = []
  
  for i in range (input_size):
    array1.append('a')
    array2.append('c')

  start = timeit.default_timer()
  #execute function here
  func(array1, array2)
  end = timeit.default_timer()
  execution_time = end-start
  
  print("This function with name {} and input size of {} took {} of execution time to complete.".format(func.__name__,input_size, execution_time))
 
#TIME BIG O(a*b) 
#SPACE BIG O(1)
timed_code(10000, slowFunction)

#TIME BIG O(1)
#SPACE BIG O(a*b)
timed_code(10000, fasterFunction)

#TIME BIG O(1)
#SPACE BIG O(a*b)
timed_code(10000, fasterFunctionSorted)

#TIME BIG O(1)
#SPACE BIG O(a*b)
timed_code(10000, reversePopFunction)

#TIME BIG O(1)
#SPACE BIG O(a*b*c*d)
timed_code(10000, anotherFunction)

