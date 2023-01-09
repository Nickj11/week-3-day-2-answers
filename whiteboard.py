# Consecutive Indices
# You are given a list of unique integers (arr), 
# and two integers (a and b). Your task is to find out whether or
#  not a and b appear consecutively in arr, and return a boolean value 
# (True if a and b are consecutive, False otherwise).
# Example:
# Input: ([3,1,0,19,4], 19, 5)	
# Output: False
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)				
# Output: True
# Input: ([3,1,0,19], 19, 0)	
# Output: True
#index of the list including intergers
#if a not inn 

def consective(nums,a,b):
    x = None
    y = None
    if a not in nums or  b not in nums:
        return False
    for i in range(len(nums)):
        if nums[i] == a:
            x=i
        elif nums[i] == b:
            y = i

    if  x -y == 1 or x-y ==-1:
        return True
    return False

    
    


print(consective([3,1,0,19,4], 19, 1))



#practice
print('hi ' + 'there') #this is cacantion
example_var = 55+32
print(example_var)
x,y = (3,5)
print(x)
print(y)


conditon = 1
while conditon < 10:
    print(conditon)
    conditon +=1

