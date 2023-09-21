import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# Task: to count number of spaces
def counts(some_texts):
    count = 0  # initialize counter value to zero
    for i in some_texts:  # incrementing counter whenever isspace() returns True
        if i.isspace():
            count = count + 1
    return count


print("The number of spaces is: ", counts(text))


def n_string(some_string):
    new_string = ''  # initialize new string
    # remove spaces and capitalize 1st letter and other letters move to lower case
    repl_text = text.strip().capitalize().replace(' iz ', ' is ').split('.')
    for m in repl_text:  # iterating elements in list
        for j in m:  # iterating elements in lists elements

            # print(j)
            if j.isspace():  # find spaces
                new_string = new_string + j  # move spaces to new string
            else:
                new_string = new_string + j.capitalize()  # capitalize 1st letter of the sentence
                new_string = new_string + m[m.find(j) + 1:]  # move the rest of sentence to new string
                new_string = new_string + m[-1].replace(m[-1], '.')  # set a dot at the end of the sentence
                break
    sentence = ' '.join(re.findall(r'\S*[.]', new_string)).replace('.', '').capitalize()
    # print(sentence)

    # join formatted text and new sentence
    res = "{} {}".format(new_string, sentence) + '.'

    return new_string


print(n_string(text))
