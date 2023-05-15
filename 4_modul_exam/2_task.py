from threading import Thread

import requests


def date1():
    data = requests.get(url="https://uztelecom.uz/")
    print(f"Status_code = {data.status_code}")


def date2():
    data = requests.get(url='https://www.pluralsight.com/guides/create-docker-images-docker-hub')
    print(f"Status_code = {data.status_code}")


def date3():
    data = requests.get(url='https://devconnected.com/create-git-branch/#Create_Git_Branch_from_Commit')
    print(f"Status_code = {data.status_code}")


def date4():
    data = requests.get(url='https://uzum.uz/uz/?utm_source=google&utm_medium=cpc&utm_campaign=uzum_uz%28tash%29_web%28desk%29_google%28dsa%29_standart&utm_content=637745822614&utm_term=&gclid=Cj0KCQjwsIejBhDOARIsANYqkD1r92n5bGPU6Nk3O7AvJQ1orUOHNjPVQHUfWU-GDauZzB-oWEKDv68aAgZ4EALw_wcB')
    print(f"Status_code = {data.status_code}")


def date5():
    data = requests.get(url='https://docs.google.com/presentation/u/0/')
    print(f"Status_code = {data.status_code}")


oqim1 = Thread(target=date1)
oqim2 = Thread(target=date2)
oqim3 = Thread(target=date3)
oqim4 = Thread(target=date4)
oqim5 = Thread(target=date5)
oqimlar = [oqim1, oqim2, oqim3, oqim4, oqim5]
for i in oqimlar:
    i.start()

for i in oqimlar:
    i.join()
