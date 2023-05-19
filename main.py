import requests
from bs4 import BeautifulSoup
from database_fill import fill_db


def get_cpus_links():
    url = 'https://www.overclockers.ua/cpu/info/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    divd = soup.find("div", id="content")
    cpus = divd.find_all("li")
    i = 0
    for name in cpus:
        for links in name:
            i += 1
            print("https://www.overclockers.ua" + name.a["href"])
            try:
                info = get_cpu_info("https://www.overclockers.ua" + name.a["href"])
                print(info)
                fill_db(info)
            except:
                break
        if i > 10:
            break


def get_cpu_info(link):
    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    inf = []
    divd = soup.find("div", id="spec")
    name = divd.find_all("th", class_="or")
    for name in name:
        inf.append(name.text)
    info = divd.find_all("tr")
    for ch in info:
        a = ch.find_all("td", class_=["gr1", "gr2"])
        for i in a:
            inf.append(i.text)
    return inf

info = get_cpu_info("https://www.overclockers.ua/cpu/info/amd/ryzen-threadripper-3960x/")
fill_db(info)