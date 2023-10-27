from datetime import datetime
import json
import os
import re
from ht4 import n_string
import xml.etree.ElementTree as et


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


# Create a function which will help the user to create his publication from json file
def read_from_json(path):
    # source_file = open(path, "r")  # open file by provided path
    json_list = json.load(open(path, "r"))
    return json_list


def get_topic_json(json_list):
    for k, v in json_list.items():
        if k == "type" and v == "News":
            text_json = json_list['text']
            city_json = json_list['city']
            res = News(text_json, city_json)
            # print(text_json)
            # res = f"News --------------------\n{f['text']}\n{f['city']}\n{date_time}\n\n"
            return res
        else:
            pass


def read_xml(path):
    tree = et.parse(open(path, "r"))
    root = tree.getroot()
    return root


def get_topic_xml(root):
    for i in root.iter():
        if i.text == 'News':
            print(i.attrib['text'])
            xml_text = i.attrib['text']
            xml_city = i.attrib['city']
            result = News(xml_text, xml_city)
            return result
            # a = f"News --------------------\n{i.attrib['text']}\n{i.attrib['city']}\n{root.date_time}\n\n"
        elif i.text == 'Private Adv':
            print(i.attrib['text'])
            xml_text1 = i.attrib['text']
            result2 = PrivateAdv(xml_text1)
            return result2
        elif i.text == 'Favorite Book':
            print(i.attrib['text'])
            xml_book = i.attrib['text']
            xml_author = i.attrib['author']
            result3 = FavoriteBook(xml_book, xml_author)
            return result3


# else:
#     result = None
# return result

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
        print(self.get_topic())
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


def publish():
    input_type = input(
        'Please choose how to get data: 1 - from file, 2 - from console: , 3 - from json file: , 4  - from XML file: ')

    # data from user provided txt file
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
    elif input_type == '3':
        try:
            path_to_file2 = input('Please provide a path to file: ')
            topic_json = read_from_json(path_to_file2)  # check which topic user selected
            topic_json2 = get_topic_json(topic_json)
            topic_json2.write_data()  # write to file
            # os.remove(path_to_file2)
        except:
            pass
    elif input_type == '4':
        try:
            path_to_file3 = input('Please provide a path to file: ')
            topic3 = read_xml(path_to_file3)  # check which topic user selected
            topic_xml = get_topic_xml(topic3)
            topic_xml.write_data()  # write to file
            # os.remove(path_to_file3)
        except:
            pass
    else:
        print('this input is not supported')


publish()
