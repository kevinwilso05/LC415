# main.py 

# Entry ponit to the test code
# We will test the soltuion class
# For LeetCode problem 415
# The solution has been provided by ...

from solutionPackage.Solution import * 

# Instantiate an object of type solution 

mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result) # Expect 579 

result = mySolution.addStrings("aaa", "bbb")
print(result)

result = mySolution.addStrings("-123", "456")
print(result)

result = mySolution.addStrings("123a", "456b")
print(result)

result = mySolution.addStrings("123!", "456@")
print(result)
'''

# Let's build a list of test cases and expected results 

num1 = ["123","999","1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]


for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else: 
        print("test failed. Change professions")