# input list of numbers comma separated and get sum of them

x = input("Enter a list of numbers separated by commas :")
sum = 0

for i in x.split(','):
    sum = sum + int(i)

print("The sum of the numbers in the list is: ", sum)
