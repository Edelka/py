# Task 1: create list of 100 random numbers from 0 to 1000
import random   # import random module

# there is used random.sample() method to generate a list of unique random numbers
a = random.sample(range(0, 1000), 100)

# Task 2: sort list from min to max (without using sort())
sorted_list = []                 # create a list for sorted results
for i in range(len(a)):          # iterating of elements
    sorted_list.append(min(a))   # move min value into the list
    a.remove(min(a))             # remove this value from list a
# print(sorted_list)
# print(a)

# Task 3 calculate average for even and odd numbers

even = []  # Create an empty list for even numbers
odd = []  # Create an empty list for odd numbers
sum_even = 0  # Create summator for even numbers
sum_odd = 0  # Create summator for odd numbers
for i in sorted_list:  # iteration
    if (i % 2) == 0:  # Verify the element is even or not
        sum_even += i   # Sum of even numbers
        even.append(i)  # Add every even number to the Even list
    if (i % 2) == 1:  # Verify the element is odd or not
        sum_odd += i  # Sum of odd numbers
        odd.append(i)  # Add every even number to the Odd list

# print(even)
# print(odd)

avg_even = sum_even / len(even)  # Calculate the average of even numbers
avg_odd = sum_odd / len(odd)  # Calculate the average of odd numbers

# Task 4 print both average result in console

print('AVG of evens and odds:', avg_even, avg_odd)   # print evens and odds
