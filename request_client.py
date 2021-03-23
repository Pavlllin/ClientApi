import requests

def Auth():
    url = 'http://127.0.0.1:8000/api/users/login/'
    print("Введите логин: ",end ="")
    login = str(input())
    print("Введите пароль: ",end ="")
    password = str(input())
    data = {"login":login, "password":password}
    r = requests.post(url,data=data)
    answer = r.json()
    return answer["token"]

def ShowNotes(token):
    url = 'http://127.0.0.1:8000/api/notes/notes/'
    headers = {
        "X-Auntification": token}
    r = requests.get(url, headers=headers)
    for n in r.json():
        print(n)

def CreateNote(token):
    url = 'http://127.0.0.1:8000/api/notes/notes/'
    headers = {
        "X-Auntification": token}
    print("Введите текст: ", end="")
    text = str(input())
    print("Введите тип файла: ",end="")
    type = str(input())
    if(type =="TXT" or type == "txt"):
        data = {"text": text, "type_of_text": 1}
        r = requests.post(url, headers=headers, data=data)
    else:
        print("Неправильный тип файла")
        CreateNote(token)

token = Auth()
ShowNotes(token)
CreateNote(token)