# Здесь указаны значения переменных, которые используются в тестах
import os
from pages.BasePage import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By

home_page_url = 'https://www.labirint.ru/'
cabinet_url = 'https://www.labirint.ru/cabinet/'

search_request = 'Островский'

book_name = 'Преступление и наказание'

valid_email = 'ivvmiller@gmail.com'
valid_code = 'E0E5-4C65-9C85'

invalid_codes = ['lgfkjhgjdlldfjkgldjkfglk',
                 '1234-5678-912q',
                 'Приветпосетитель',
                 'hdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfje',
                 '123456789123',
                 '1865-44DF-B712'
                 ]
ids_invalid_codes = ['Рандомная строка',
                     'Строка верной длинны',
                     'Кирилица',
                     'Строка > 256 символов',
                     'Строка из цифр',
                     'Код верного формата'
                     ]

invalid_codes_spec = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']']
ids_invalid_codes_spec = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']']

fio1 = 'Иванов Иван Иванович'
fio2 = 'Петров Петр Петрович'


class pages(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/books/'

        super().__init__(web_driver, url)

    button_genres = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[1]/a')
    button_kids = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[2]/a')
    comic_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[3]/a')
    youth_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[4]/a')
    fiction_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[5]/a')
    periodic_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[6]/a')
    religion_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[7]/a')
    dict_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[8]/a')
    art_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[9]/a')
    exc_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[10]/a')
    trans_2 = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[6]/div[2]/div[1]/div[2]/div[2]/a')
    trans_10 = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[6]/div[2]/div[1]/div[2]/div[10]/a')