import requests
from bs4 import BeautifulSoup



def getInfo():
    site = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/")

    if site.status_code != 200:
        return "Извините, в данный момент информация недоступна."
    html = site.text

    soup = BeautifulSoup(html, features="html.parser")
    # ill_count = soup.find('div', class_="cv-countdown__item-value _accent").text
    # day_ill_count = soup.fint('div', class_="")

    all = soup.find_all('div', class_="cv-countdown__item-value")
    # all = soup.find_all('div', class_="cv-countdown__item-value _accent")

    tests = all[0].text
    ill = all[1].text
    day_ill = all[2].text
    heal = all[3].text
    dead = all[4].text
    info = "На данный момент в России по коронавирусу ситуация следующая:\n" \
           "Проведено тестов: {}\n" \
           "Случаев заболевания: {}\n" \
           "Случаев заболевания за последние сутки: {}\n" \
           "Выздоровевших: {}\n" \
           "Умерших: {}.".format(tests, ill, day_ill, heal, dead)
    return info

