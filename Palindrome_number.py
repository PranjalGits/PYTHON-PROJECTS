def is_palindrome(number):
    # Convert the number to a string for easier manipulation
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    if number_str == number_str[::-1]:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome!")
else:
    print(num, "is not a palindrome.")