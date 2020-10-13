import requests
from bs4 import BeautifulSoup

# Agent
header = {

    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'

}

# Link
link = 'https://warsonline.info'

###
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')

# Blocks
block = soup.find('div', id='content_outmiddle')
close_block = block.find('div', id='nsp-nsp-112')
ul_block = close_block.find('ul', class_='nspList active nspCol1')

# Вот эта штука является ключом ко всему!
# Спустя час это заработало так, как надо
links_amount = 9
massive = []
for i in range(0, links_amount):
    li_block = ul_block.find_all('li')[i]
    # Header of block
    h4_h = li_block.find('h4').text
    # Body of block
    b_of_block = li_block.find('p').text

    f = f'{h4_h}.'  f'{b_of_block}' '\n'
    massive.append(f)


    # Это работает!
    # print(li_block)
    print(f)

    ##ОН УДАЛЯЕТ ВСЕ, ЧТО БЫЛО РАНЬШЕ! writelines позволяет считать данные из массива
with open('parsed.txt','w') as file:
    file.writelines(massive)



