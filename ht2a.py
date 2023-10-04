# Task 1: 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random  # import random module
import string

# create empty list and call it dict_list
dict_list = []
# for each iteration create random number of dictionaries (randint from random library)
for i in range(random.randint(2, 4)):
    # create random dictionary size and assign it to size variable
    dict_size = random.randint(2, 4)
    # create random letters for keys (using string library's ascii_lowercase method)
    keys = random.sample(string.ascii_lowercase, dict_size)
    # create random numbers from 0 to 100 assign it to values variable for each dict which are inside of list
    values = (random.randint(0, 101) for k in range(dict_size))
    # convert to key-value pairs
    dictionary = dict(zip(keys, values))
    # print(dictionary)
    # add created dictionaries to dict_list
    dict_list.append(dictionary)

print(dict_list)

keys_list = []                        # creating a list for keys
for d in dict_list:
    keys_list.extend(list(d.keys()))  # list(d.keys() converting to list
#    print(keys_list)

keys_set = set(keys_list)
# print(keys_set)

final_dict = {}                      # creating a final list
for k in keys_set:                   # iterating in list of keys
    temp_list = []                   # creating a temp list of all values for each key
    for i in dict_list:              # iterating through dictionaries in dict_list
        if k in i.keys():            # check if key is in dictionary, then put it to temp_list
            temp_list.append(i[k])
        else:
            temp_list.append(-1)     # if key is NOT in dictionary, then put '-1' to temp_list
    # print(k)
    # print(temp_list)
    if len([j for j in temp_list if j != -1]) == 1:      # check if element of temp_list != -1, as result we have len()=1
        final_dict[k] = max(temp_list)                   # write max value from temp_list for key
    else:
        ind = temp_list.index(max(temp_list)) + 1        # get the index of key with max value
        k = k + '_' + str(ind)                           # add a suffix for key
        final_dict[k] = max(temp_list)                   # write max value for key
print(final_dict)





