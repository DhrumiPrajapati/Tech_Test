#function for palindrome
def palindrome(string):
    return string == string[::-1]

testString = input("Enter the string : ")
check = palindrome(testString)

if check:
    print("True")
else:
    print("False")