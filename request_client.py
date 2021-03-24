from dataclasses import dataclass
from typing import List

import requests


@dataclass
class NoteJSON:
    text: str
    type_of_text: int


class PastebinClientApi():
    def __init__(self, login: str, password: str, url: str):
        self.login = login
        self.password = password
        self.url = url
        self.session = requests.Session()
        self.timeout = 5
        self.token = self.auth()


    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()

    def auth(self) -> str:
        url = self.url + '/api/users/login/'
        data = {"login": self.login, "password": self.password}
        r = self.session.post(url, data=data, timeout=self.timeout)
        answer = r.json()
        return answer["token"]

    def show_notes(self) -> List[NoteJSON]:
        url = self.url + '/api/notes/notes'
        headers = {
            "X-Auntification": self.token}
        r = self.session.get(url, headers=headers, timeout=self.timeout)
        return r.json()

    def create_note(self, text: str, type: str):
        url = self.url + '/api/notes/notes/'
        headers = {
            "X-Auntification": self.token}
        if (type == "TXT" or type == "txt"):
            data = {"text": text, "type_of_text": 1}
            r = self.session.post(url, headers=headers, data=data, timeout=self.timeout)
        else:
            print("Неправильный тип файла")

    def create_note_from_file(self, path: str):
        url = self.url + '/api/notes/notes/'
        headers = {
            "X-Auntification": self.token}
        type = path[path.find(".") + 1:]
        text = ""
        with open(path) as file:
            for line in file:
                text += line
        if (type == "TXT" or type == "txt"):
            data = {"text": text, "type_of_text": 1}
            r = self.session.post(url, headers=headers, data=data, timeout=self.timeout)
        else:
            print("Неправильный тип файла")

    def close(self):
        self.session.close()

api = PastebinClientApi("A", "A", "http://127.0.0.1:8000")
api.show_notes()
api.close()


with PastebinClientApi("A", "A", "http://127.0.0.1:8000") as api:
    api.show_notes()
