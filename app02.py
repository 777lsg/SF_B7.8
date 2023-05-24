import urllib.request

#Или вводить вручную или скачивает статическую ссылку

#url = "https://ru.wikipedia.org/favicon.ico"
url = input("Введите URL для скачивания: ")
destination = "/app02/favicon.ico"

urllib.request.urlretrieve(url, destination)

print("Файл успешно скачан.")