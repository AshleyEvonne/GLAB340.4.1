#Input: take a number fromt the user
number= int(input("Enter a number: "))

#Convert the number to a string for easier comparsion
num_str = str(number)

#Reverse the string 
reversed_str = num_str[::-1]

#Check if original number and its reverse are the same 
if num_str == reversed_str:
    print(f"{number} is a plaindrome number.")
else:
    print(f"{number} is not a palindrome number.")

n = 5
for i in range(n):
    for j in range(i):
        print('*', end = "")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end = "")
    print('')