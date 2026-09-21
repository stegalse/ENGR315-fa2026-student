import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
# sorted_list = sorted(even_list) #sort the list in ascending order and assign it to sorted_list
# print("The sorted list is: ", sorted_list) #print out the sorted list

list_length = len(even_list) #find the length of the list and assign it to list_length
middle_index = list_length//2 # calculate the middle index of the list and assign it to middle_index
first_middle = even_list[middle_index] #find the first middle value

second_middle_index = middle_index - 1 # calculate the second middle index of the list 
second_middle = even_list[second_middle_index] #find the second middle value
print("The middle values are:", second_middle, "and", first_middle) #print out the two middle values of the list

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (first_middle + second_middle) / 2 #calculate the average of the two middle values

# the average of middle elements is
print("The average is: ", middle_average)
