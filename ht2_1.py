import random  # import random module
import string  # import string library

# create 1st dictionary with 5 elements
d1 = {k: random.randint(1, 99) for k in random.sample(string.ascii_lowercase, 5)}
# print(d1)
# create 2nd dictionary with 5 elements
d2 = {k: random.randint(1, 99) for k in random.sample(string.ascii_lowercase, 5)}
# print(d2)

dict_list = [d1, d2]  # creation of dictionary list
print(dict_list)  # print the list

d1_keys = []  # initiate a list of keys for d1 dict
d2_keys = []  # initiate a list of keys for d2 dict
result = {}  # initiate a dict for result

# Separate keys from d1
for key, value in d1.items():
    keys1 = key
    d1_keys.append(keys1)  # move key to d1_keys
# print(d1_keys)

# Separate keys from d2
for key, value in d2.items():
    keys2 = key
    d2_keys.append(keys2)  # move key to d2_keys
# print(d2_keys)
a = 0   # set variable to define number of items
# Check if key in d1 == key in d2
while a < len(d1_keys):
    if d1_keys[a] == d2_keys[a]:
        # Find the highest value for key in d1,d2:
        for i in d1_keys[a]:   # iterating
            if d1[i] > d2[i]:  # comparing values in d1 and d2
                result[i] = d1[i]  # Put the highest value in result map from d1
                result['{}_1'.format(i)] = result.pop(i)  # Change key format
            else:
                result[i] = d2[i]  # Put the highest value in result map from d2
                result['{}_2'.format(i)] = result.pop(i)  # Change key format
        a = a + 1
    # If key from d1 not in d2, then put both keys and values in result:
    else:
        result[d1_keys[a]] = d1[d1_keys[a]]
        result[d2_keys[a]] = d2[d2_keys[a]]
        a = a + 1

print(result)   # print result
