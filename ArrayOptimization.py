//The task is to find if the two separate arrays have common items and return true if this is the case. Else return false.


def slowFunction(array1, array2):

  array1 = ['a','b','f','g']
  array2 = ['e','k','l','b']

  for item in array1:
    for val in array2:
      if item == val:
        print("found "+ val)
        return true

  return false

def fasterFunction(array1, array2):

  // remove duplicates from both arrays
  array1_singles = list(dict.fromkeys(array1)) //convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates
  array2_singles = list(dict.fromkeys(array2)) //convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates

  for item in array1:
    for val in array2:
      if item == val:
        print("found "+ val)
        return true

  return false

def fasterNotNestedFunction(array1, array2):

  // remove duplicates from both arrays
  array1_singles = list(dict.fromkeys(array1)) //convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates
  array2_singles = list(dict.fromkeys(array2)) //convert list to dict and back because dict cant contain duplicate keys so gets rid of duplicates

  

give letters numerical representations
array1_as_numerical = []
array2_as_numerical = []

for character in array1_singles:
    number = ord(character) - 96
    array1_as_numerical.append(number)

for character in array2_singles:
    number = ord(character) - 96
    array2_as_numerical.append(number)

//sort the array ascending
array1_as_numerical.sort()
array2_as_numerical.sort()

//example1 list [1,4,20,23]
//example2 list [2,3,17,20]
//because lists are sorted can check if target is bigger than item and break the inner loop immediately, else if smaller continue, else its a match

for item in example1:
  for target in example2:
    if target > item:
      break
    elif target < item:
      continue
    else:
      return true

return false


//proposed solution is create an object of array1 and check if object contains array2 items, so moving from O(a^2) to O(a)

def firstArrayAsObject(array1, array2):



