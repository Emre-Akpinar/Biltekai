import numpy as np



"""
a_mul = np.array([[[1,2,3, 1],
                  [4,5,6, 1],
                  [7,8,9, 1]],
                  [[1,1,1,1],
                  [0,0,0,0],
                  [1,1,1,1]]])
print(a_mul.shape) #showing the shape of the array
print(a_mul.ndim) #showing the dimensions array has
print(a_mul.size) #Size of the array. Basically multiplying the shape values
print(a_mul.dtype) #Why we care about the data type bcuz  nump written in C. Let's see an example why:

a = np.array([[1,2,3],
             [4,"Hello",6],
             [4, 5, 1]])
print(a.dtype) #The array now has a type string and all of the elements are string
print(type(a[0][0])) #as you see initally int 1 is now a string
"""

           #Functions


#full, zeros and ones
"""
a = np.full((2,3,4),7)
print(a)
print()
print()


a = np.zeros((4,5,2))
print(a)
print()
print()

a = np.ones((3,4,2))
print(a)
"""

#arange,linspace
"""
x_values = np.arange(0,1001,5) #adds 5 to variable and adds it
print(x_values)

x_values = np.linspace(0,1000,5) #Divides the interval to 5 and prints the values
print(x_values)
"""

#nan and inf
"""
print(np.nan)
print(np.inf)

print(np.isnan(np.sqrt(-1))) #np.isnan() checks the value and prints true if it is not a number
print(np.isinf(np.array([10])/0)) #np.isinf() checks the value and prints true if it is infinite number
                                  #and it wouldnt work if there was a 10/0 instead of np.array([10])/0
"""


            #Performing math operations with numpy
"""
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5) #repeats the list 5 times
print(a1 * 5) #does actual calculation for all the items

#print(l1 + 5) #Gives error because you cant concatenate int with list
print(a1 + 5) #again, it does calculation


print(l1 + l2) #That essantially takes l2 and adds after l1 in one list
print(a1 + a2) #Adds same indexed elements
print(a1 * a2)
print(a1 - a2)
print(a1 / a2) #This is gonna give RunTimeWarning because there is a 0 in the a2


#syntax errors
#print(l1 - l2)
#print(l1 * l2)
#print(l1 / l2)
"""
































