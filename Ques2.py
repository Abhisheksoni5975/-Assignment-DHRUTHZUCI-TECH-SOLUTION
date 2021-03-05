# Question 2:
# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
 
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.

# Answer:

x1 = [int(item) for item in input("Enter the number subsequently: ")] #Taking input for list1 using list comprehension and storing it in x1
x2 = [int(item) for item in input("Enter the number subsequently: ")] #Taking input for list2 using list comprehension and storing it in x2
print("Input1:"+ str(x1))
print("Input2:"+ str(x2))
s1=set(x1)#Typecasting the list into SET
s2=set(x2)#Typecasting the list into SET
print('Output' +str(s1.intersection(s2)))#Performing the intersection using set method

