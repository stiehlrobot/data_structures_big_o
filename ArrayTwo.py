import timeit
import inspect
import time
import types
from typing import cast

#merge sorted arrays

#BIG O(a)
def mergeSortedArrays(array1, array2):

    if(len(array1) == 0 and len(array2) == 0):
        return array1
    elif(len(array1) == 0 and len(array2) > 0):
        return array2
    elif(len(array1) > 0 and len(array2) == 0):
        return array1
    else:
        mergedArray = array2
        for item in array1:
            mergedArray.append(item)
            mergedArray.sort()        




    



def mergeSortedArrays2(array1, array2):

    if(len(array1) == 0 and len(array2) == 0):
        return array1
    elif(len(array1) == 0 and len(array2) > 0):
        return array2
    elif(len(array1) > 0 and len(array2) == 0):
        return array1
    else:
        mergedArray = array1 + array2
        mergedArray.sort()
    


def mergeSortedArrays3(array1, array2):
    if(len(array1) == 0 and len(array2) == 0):
        return array1
    elif(len(array1) == 0 and len(array2) > 0):
        return array2
    elif(len(array1) > 0 and len(array2) == 0):
        return array1
    else:
        array1.extend(array2)
        array1.sort()
    

def timed_code(input_size, func):

  array1 = []
  array2 = []
  
  for i in range (input_size):
    array1.append('3')
    array1.append('4')
    array2.append('6')
    array2.append('7')

  start = timeit.default_timer()
  #execute function here
  func(array1, array2)
  end = timeit.default_timer()
  execution_time = end-start
  
  print("This function with name {} and input size of {} took {} of execution time to complete.".format(func.__name__,input_size, execution_time))


timed_code(10000,mergeSortedArrays)
timed_code(10000,mergeSortedArrays2)
timed_code(10000,mergeSortedArrays3)