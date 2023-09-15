import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# Text formatting
# remove spaces and capitalize 1st letter and other letters move to lower case
ch_text = text.strip().capitalize()
# print(ch_text)
# change 'iz' with 'is'
repl_text = ch_text.replace(' iz ', ' is ').split('.')

# print(repl_text)

new_string = ''          # initialize new string
for i in repl_text:      # iterating elements in list
    for j in i:          # iterating elements in lists elements
        # print(j)
        if j.isspace():                      # find spaces
            new_string = new_string + j      # move spaces to new string
        else:
            new_string = new_string + j.capitalize()             # capitalize 1st letter of the sentence
            new_string = new_string + i[i.find(j) + 1:]          # move the rest of sentence to new string
            new_string = new_string + i[-1].replace(i[-1], '.')  # set a dot at the end of the sentence
            break
# print(new_string)
# print(repl_text)

# find the last word in each sentence, remove dots, upper case to 1st letter
sentence = ' '.join(re.findall(r'\S*[.]', new_string)).replace('.', '').capitalize()
# print(sentence)

# join formatted text and new sentence
res = "{} {}".format(new_string, sentence) + '.'
print(res)

# Task: to count number of spaces
count = 0  # initialize counter value to zero
for i in text:  # incrementing counter whenever isspace() returns True
    if i.isspace():
        count = count + 1
print("The number of spaces is: ", count)
