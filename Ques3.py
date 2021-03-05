# Question 3:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
 
# Example 2:
# Input: "()[]{}"
# Output: true
 
# Example 3:
# Input: "(]"
# Output: false
 
#   Answer:

a=input()
a1, a2, a3, a4, a5, a6=0,0,0,0,0,0
if(a==""):
    print("True")
else:
    for i in range(len(a)):
        if(a[i]=='('):
            a1+=1
        elif(a[i]==')'):
            a2+=1
        elif(a[i]=='{'):
            a3+=1
        elif(a[i]=='}'):
            a4+=1
        elif(a[i]=='['):
            a5+=1
        elif(a[i]==']'):
            a6+=1
        else:
            print("false")  
    if(a1==a2 and a3==a4 and a5==a6):
        print("true")
    else:
        print("false")
