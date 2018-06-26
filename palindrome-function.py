# Write a function is_palindrome(string) that returns true or false that performs the following task:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example, "Red rum, sir, is murder" is a palindrome, while "Programcreek is awesome" is not.


#Create variables to test accuracy of created function
true_test = "Red rum, sir, is murder"
false_test = "Programcreek is awesome"

true_test2 = "A man, a plan, a canal: Panama"
false_test2 = "My name is Austin Kegarise"

#Create function
def is_palindrome(string):

    #Convert given string to the same case
    clean_string = string.casefold()
    
    #Loop through "clean_string"
    for i in range(len(clean_string)):
        if clean_string[i] != clean_string[-1-i]:
            return False
        else:
            return True
        
#Display results of tests
print(is_palindrome(true_test))
print(is_palindrome(false_test))
print(is_palindrome(true_test2))
print(is_palindrome(false_test2))

