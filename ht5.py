from datetime import datetime
from quo import echo

# Create 'News' class with date calculating
class News:
    def __init__(self, text, city, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
        self.text = text
        self.city = city
        self.date_time = date_time


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


# Crate 'FavoriteBook' class
class FavoriteBook:
    def __init__(self, text, author):
        self.text = text
        self.author = author


# Create a function which will help the user to create his publication
def publish():
    n = input('Choose your topic (1 as News, 2 as Private Adv, 3 as Favorite Book): ')
    try:
        if n == '1':
            news = News(input('Your text: '), input('City: '))
            result = (
                f"News --------------------\n{news.text}\n{news.city}, {news.date_time}\n")
        elif n == '2':
            private_adv = PrivateAdv(input('Your text: '))
            result = (
                f'Private Adv --------------\n{private_adv.text}\nActual until: {private_adv.date_time()}\n')
        elif n == '3':
            favorite_book = FavoriteBook(input('Your book: '), input('Author: '))
            result = (
                f'Favorite Book -------------\n{favorite_book.text}\nAuthor: {favorite_book.author}\n')
        return result
    except:
        print('This topics type is not supported.')


p = publish()


# Create a function that will write new publications to the file
def to_file():
    try:
        f = open('C:/Users/Olena_Pakholchak/Desktop/New folder (2)/newsfeed.txt', 'a')
        f.write(p + '\n\n\n')
        f.close()
    finally:
        print('If you want please repeat again with new topics.')


to_file()
