import requests as rq
from bs4 import BeautifulSoup

url = 'https://стопкоронавирус.рф'

responce = rq.get(url).text
soup = BeautifulSoup(responce, 'html.parser')

block1 = soup.find('div', class_='cv-banner__container _g-outer-width _g-inner-padding')
block2 = block1.find('div', class_='cv-banner__content')
block3 = block2.find('div', class_='cv-banner__bottom')
block4 = block3.find('div', class_='cv-countdown')
block5 = block4.find_all('div', class_='cv-countdown__item')[2]
block6 = block5.find('div', class_='cv-countdown__item-value _accent')
block7 = block6.find('span').text

peoples = []
count = 0


if block7 not in peoples:
    peoples.append(block7)
    last_people = peoples[count]
    pr = f'Выявлено заболевших за последние сутки: {last_people} \n'
    print(count)
    print(pr)
    count += 1
else:
    print(f'Выявлено заболевших за последние сутки: {peoples} \n  ELSE')





with open('../../../PycharmProjects/pythonProject1/venv3.7/covid.txt', 'w') as file1:
    file1.write(pr)
