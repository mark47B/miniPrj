import urllib.request as urllib


def getPage(url, parm=None):
    resp = urllib.urlopen(url)
    if resp.code == 200:
        return resp.read().decode('utf-8')
    else:
        print("Site unavailable!!! /n")


def parsePageD(html):
    html = html[html.find('B настоящее время на факультете работает 21 кафедра:'):html.find('<!-- end main -->')]
    html = html[html.find('<ol>'):html.find('</ol>')]
    depts = []
    while(html.find('<li>') != -1):
        html = html[html.find('<a href='):]
        html = html[html.find('>') + 1:]
        depts.append(html[:html.find('</')])
    return depts


def parsePageS(html):
    html = html[html.find('<table'):html.find('</table')]
    staff = []
    while(html.find('<tr>') != -1):
        html = html[html.find('<td>') + 4:]
        buff = html[:html.find('</td>')]
        if buff.find('<a') != -1:
            html = html[html.find('<a href='):]
            html = html[html.find('>') + 1:] 
        staff.append(html[:html.find('</')])
        html = html[html.find('<tr>'):]
    return staff


url = "http://www.apmath.spbu.ru/ru/structure/depts/"
htmlDepts = getPage(url)
depts = parsePageD(htmlDepts)

url = "http://www.apmath.spbu.ru/ru/staff/"
htmlStaff = getPage(url)
staff = parsePageS(htmlStaff)

while(True):
    print('Enter \'1\' if you want to get a list of tutors \
        \nEnter \'2\' if you want to get a list of departments \
        \nEnter \'3\' if you want to exit')
    a = input()
    if a == '1':
        n = 0
        for i in staff:
            n = n + 1
            print(f'{n}. {i}')
        print('\n \n')
    elif a == '2':
        n = 0
        for i in depts:
            n = n + 1
            print(f'{n}. {i.capitalize()}')
        print('\n \n')
    elif a == '3':
        break


'''
lstDepts = open('depts.txt', 'w')
lstDepts.write(firstPage)
'''