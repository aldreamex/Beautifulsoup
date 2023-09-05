import re
from bs4 import BeautifulSoup

with open('blank/index.html', encoding='utf-8') as file:
    src = file.read()
print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)            #<title>Главная страница блога</title>
print(title.text)       #Главная страница блога
print(title.string)     #Главная страница блога

#____________________методы find и find_all______________

page_h1 = soup.find("h1")   #выводит первый нужный обьект(сверху вниз) - <h1>Страница пользователя Mr. Anderson</h1>
print(page_h1)

page_all_h1 = soup.find_all("h1")   #выводит все элементы в список (сверху вниз) - [<h1>Страница пользователя Mr. Anderson</h1>, <h1>Еще один h1 заголовок</h1>]
print(page_all_h1)

for perebor_vivod in page_all_h1:   #Страница пользователя Mr. Anderson
    print(perebor_vivod.text)       #Еще один h1 заголовок

user_name = soup.find('div', class_="user__name")
print(user_name.text.strip())

user_name1 = soup.find('div', {'class': 'user__name'}).find('span').text
print(user_name1)

#соберем все данные тега span
find_all_spans_in_user_info = soup.find(class_='user__info').find_all('span')
print(find_all_spans_in_user_info)

for iten in find_all_spans_in_user_info:    #перебор списка и вывод текста
    print(iten.text)

#парсим ссылки на соц. сети пользователя указывая будь до нужной информации (класс, список, тег)
social_links = soup.find(class_='social__networks').find('ul').find_all('a')
print(social_links)

#парсим ссылки на соц. сети сразу со всей страницы
all_a = soup.find_all('a')
print(all_a)
for item in all_a:    #перебор списка и вывод текста
    item_text = item.text
    item_url = item.get('href')
    print(f'{item_text}: {item_url}' )  #inst: ссылка; twit: ссылка...;

#____________________методы .find_parent() и .find_parents()______________

#собираем инфу из статьи идя этими методами снизу вверх
post_div = soup.find(class_='post__text').find_parent() #забираем блок до первого родителя
print(post_div)

post_divs = soup.find(class_='post__text').find_parents() #забираем блок до первого родителя
print(post_divs)

#____________________методы .next_element() и .previous_element()______________
#next - двигается пошагово сверху вниз и возвращает следующий элемент в коде
next_el = soup.find(class_='post__title').next_element.next_element.text
print(next_el)

next_ell = soup.find(class_='post__title').find_next().text
print(next_ell)

#previous - двигается пошагово снизу вверх и возвращает следующий элемент в коде
# previous_el = soup.find(class_='post__title').previous_element.previous_element.text
# print(previous_el)

#____________________методы .find_next_sibling() и .find_previous_sibling()______________
#ищут и возвращают следующие и предыдущие элементы внутри искомого тега
next_sib = soup.find(class_='post__title').find_next_sibling()
print(next_sib)