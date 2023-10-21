import csv
from collections import Counter
import pandas

path = r'C:/Users/Olena_Pakholchak/PycharmProjects/pnew1/modules/newsfeed.txt'


def get_words_letters(path_to_file):
    with open(path_to_file, 'r') as f:
        rows_from_file = [str(i) for i in f.readlines()]
        # print(rows_from_file)
        f.close()

    words = []
    letters = []
    for i in rows_from_file:
        every_line = i.replace('!', ',').replace('?', ',').replace(' ', ',').replace('.', ',').replace('\n',
                                                                                                       ',').replace(':',
                                                                                                                    ',').replace(
            '&', ',')
        new_rows = every_line.split(',')

        for word in new_rows:
            if word.isalpha():
                words.append(word.lower())
                for letter in word:
                    letters.append(letter)

    return words, letters


def count_words_letters(w, l):
    count_words = dict(Counter(w))
    count_letters = dict(Counter(l))
    return count_words, count_letters


words_list, letters_list = get_words_letters(path)
counts_words, counts_letters = count_words_letters(words_list, letters_list)


# print(words_list)
# print(letters_list)
# print(counts_words)
# print(counts_letters)


def words_count_csv():
    with open('words_count1.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='-')
        w.writerows(counts_words.items())


def count_upper_l(dictionary):
    d = {}
    for letter, count in dictionary.items():
        if letter.isupper():
            d[letter] = count
        else:
            d[letter] = 0

    return d


count_of_upper_case = count_upper_l(counts_letters)


# print(count_of_upper_case)


def percent_of_total(dictionary):
    d = {}
    total_count = sum(dictionary.values())
    for letter, count in dictionary.items():
        perc = count * 100.0 / total_count
        d[letter] = perc

    return d


percent = percent_of_total(counts_letters)


# Statistics for letters
def stat_csv():
    letter = [*counts_letters.keys()]
    count = [*counts_letters.values()]
    count_up_case = [*count_of_upper_case.values()]
    pct = [*percent.values()]

    final = {'Letter Name': letter, 'Count All': count, 'Count Uppercase': count_up_case, 'Percents': pct}

    pd1 = pandas.DataFrame(final)
    # index_ = letter
    # pd1.index = index_
    pd1.to_csv("letters_stat.csv", sep='|')


words_count_csv()
stat_csv()
