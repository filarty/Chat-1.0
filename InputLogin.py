import PySimpleGUI as pg
from JsonProtocol import Protocol


class InputLogin:
    def __init__(self):
        self.pg = pg

    def create_window(self):
        layout = [
            [pg.InputText(size=(37, 30))],
            [self.pg.Button("Send", bind_return_key=True, font=10)]
        ]
        window = self.pg.Window("Login", layout)
        return window

    def main(self):
        window = self.create_window()
        login = None

        while True:
            event, count = window.read(timeout=1000)
            if event == pg.WIN_CLOSED:
                break
            if event == "Send":
                login = count[0]
                break

        window.close()
        return login

