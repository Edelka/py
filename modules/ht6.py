from datetime import datetime
import sys
import os
import re
from ht4 import n_string


def read_topics(path):
    source_file = open(path, "r")  # open file by provided path
    lines = source_file.readlines()  # read the lines in the file
    lines = [i.rstrip('\n') for i in lines]  # cut empty line 'News\n'
    print(lines)
    if lines[0] == 'News':  # check if the 1st line is News
        text = lines[1]  # set text as line 2
        city = lines[2]  # set city as line 3 from file
        news = News(text, city)  # initialize class exemplar
        return news
    elif lines[0] == 'Private Adv':
        text = lines[1]
        pr_adv = PrivateAdv(text)
        return pr_adv
    elif lines[0] == 'Favorite Book':
        text = lines[1]
        author = lines[2]
        fav_book = FavoriteBook(text, author)
        return fav_book


# Create 'News' class with date calculating
class News:
    def __init__(self, text, city, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
        self.text = text
        self.city = city
        self.date_time = date_time

    # getting data for the following writing it to file
    def get_topic(self):
        result = f"News --------------------\n{self.text}\n{self.city}, {self.date_time}\n\n"
        return result

    # write to file function
    def write_data(self):
        with open("newsfeed.txt", "a") as file:
            # body_t = self.get_topic()
            # s = n_string(body_t)
            # print(s)
            file.write(self.get_topic())  # write content of get_topic() to file


# Create 'PrivateAdv' class
class PrivateAdv:
    def __init__(self, text):
        self.text = text

    def date_time(self):
        str_d1 = input('Please type "Actual until" date in format: dd/md/YY: ')

        # Convert string data type to datetime datatype for input date
        date1 = datetime.strptime(str_d1, "%d/%m/%Y")
        # Double convertion for publish date (datetime-string-datetime)
        date2 = datetime.now().strftime("%d/%m/%Y")
        dt = datetime.strptime(date2, "%d/%m/%Y")

        # Calculate the difference between dates in timedelta
        delta = date1 - dt
        return f'{delta.days} days left'

    def get_topic(self):
        result = f'Private Adv --------------\n{self.text}\nActual until: {self.date_time()}\n\n'
        return result

    def write_data(self):
        with open("newsfeed.txt", "a") as file:
            file.write(self.get_topic())


# Create 'FavoriteBook' class
class FavoriteBook:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def get_topic(self):
        result = f'Favorite Book ------------\n{self.text}\nAuthor: {self.author}\n\n'
        return result

    def write_data(self):
        with open("newsfeed.txt", "a") as file:
            file.write(self.get_topic())


# Create a function which will help the user to create his publication
def publish():
    input_type = input('Please choose how to get data: 1 - from file, 2 - from console: ')
    n = input('Choose your topic (1 as News, 2 as Private Adv, 3 as Favorite Book): ')
    # data from user provided file
    if input_type == '1':
        try:
            path_to_file = input('Please provide a path to file: ')
            topic = read_topics(path_to_file)  # check which topic user selected
            topic.write_data()  # write to file
            # os.remove(path_to_file)
        except:
            pass
    # data from user's input in console
    elif input_type == '2':
        n = input('Choose your topic (1 as News, 2 as Private Adv, 3 as Favorite Book): ')
        try:
            if n == '1':
                news = News(input('Your text: '), input('City: '))
                news.write_data()
            elif n == '2':
                private_adv = PrivateAdv(input('Your text: '))
                private_adv.write_data()
            elif n == '3':
                favorite_book = FavoriteBook(input('Your book: '), input('Author: '))
                favorite_book.write_data()
            else:
                print('This topics type is not supported.')
        except:
            print('Please try again.')
    else:
        print('this input is not supported')


publish()
