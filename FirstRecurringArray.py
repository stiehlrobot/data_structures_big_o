#Given an array of numbers, return first recurring number in array
#eg [2,4,6,7,4,6,8,9]
#should return 4

#Time complexity O(n)

def first_recurring_number(array):

    numbers_found = []
    for item in array:
        if item in numbers_found:
            return item
        if item not in numbers_found:
            numbers_found.append(item)
    return None

#Time complexity O(n)

def first_recurring_number2(array):

    looped_nums = {}
    for item in array:
        #if item in looped_nums:
        if looped_nums.get(item) is True:
            return item
        else:
            looped_nums[item] = True
    
    return None
    #make into dict
    #know what numbers can be 



numbers = [9,9,1,2,3,5,1,3,4]
num1 = []
num2 = [1]
num3 = [0,1,2,3,4,5,6,7,8,9,0]

print(first_recurring_number2(numbers))
print(first_recurring_number2(num1))
print(first_recurring_number2(num3))
