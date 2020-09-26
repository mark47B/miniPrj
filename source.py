import urllib.request as urllib
import re


def get_page(url, parm=None):
    resp = urllib.urlopen(url)
    if resp.code == 200:
        return resp.read().decode('utf-8')
    else:
        print("Сайт недоступен /n")


def parse_page(html):
    if html.find('<ol>') != -1:
        html = html[html.find('<ol>'):html.find('</ol>')]
    elif html.find('<table') != -1:
        html = html[html.find('<table'):html.find('</table>')] 
    depts = re.findall(r'[А-я, ё,\s,-]{11,1000}', html)
    return depts


def print_list(current_list):
    n = 0
    for i in current_list:
        n = n + 1
        print(f'{n}. {i.capitalize()}')


url = "http://www.apmath.spbu.ru/ru/structure/depts/"
html_depts = get_page(url)
depts = parse_page(html_depts)

url = "http://www.apmath.spbu.ru/ru/staff/"
html_staff = get_page(url)
staff = parse_page(html_staff)

num_to_list = {'1': staff, '2': depts}

while(True):
    print('Введите \'1\' если вы хотите получить список преподавателей\n\
Введите \'2\' если вы хотите получить список кафедр\n\
Введите любой символ, кроме написанного выше, чтобы выйти')
    a = input()
    if re.fullmatch(r'\b[1-2]{1}\b', a) is not None:
        print_list(num_to_list[a])
    else:
        break
