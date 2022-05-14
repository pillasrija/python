# Write a 'while' loop that prints integers from zero to 5

i=1
while(i<=5):
    print(i)
    i +=1


"""
Write a while loop that starts at the last character in the string and works
its way backwards to the first character in the string, printing each letter
on a separate line, except backwards
"""

word = 'jiyansh'
index = len(word) - 1
while index >= 0:
    letter = word[index]
    print(letter)
    index -= 1

# Write a program that asks the user to enter a number and prints out all the divisors of that number.

n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)

# Factorial of any number n is represented by n! and is equal to 1 * 2 * 3 * .... * (n-1) * n.

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


num = 4;
print("Factorial of", num, "is",
      factorial(num))

# Write a program to calculate factorial of any given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers

def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

# Write a program to print whether the given number is a palindrome or not.

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


# Write a program that uses list and range to create the list [3,6, 9, . . . , 99] .
for i in range(3,100,3):
    print(i, end =" ")

# Write a program to convert a list of characters into a single string.

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

# Write a program to read a string from the user and print the list of characters in the string.
s = 'abcd'
print("actual string:",s)
print("converted to list:\n",list(s))

# Write a Python program to find common items from two lists
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

# Write a Python program to get the difference between the two lists.

list1 = [1, 2 ,3 ,4]
list2=[1, 2]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

# Write a Python program to get the largest number from a list.
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

# Write a Python program to find the second smallest number in a list.
def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[1]

print(second_smallest([1, 2, -8, -2, 0]))

# Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

# Write a Python program to sum all the items in a list.
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

# Write a Python program to multiply all the items in a list.

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,3,4]))

# Write a program to print the list of numbers which are greater than the average of numbers in the following list.

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average([2, 4, 3, 9, 13, 12, 7, 6, 1, 5]))

# Write a program to print a new list containing squares of each element in the following list.

numbers = [3,7,11,12,17,21]

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)

# Write a program to know how many times an element occurred in the list.

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


lst = [5, 10, 15, 20, 25, 50, 20]
x = 20
print('{} has occurred {} times'.format(x, countX(lst, x)))

















