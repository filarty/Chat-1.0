from threading import Thread
import PySimpleGUI as pg
import socket
from JsonProtocol import Protocol
from InputLogin import InputLogin


class Client:
    def __init__(self, pg: pg) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pg = pg
        self.__window = None
        self.users = None
        self.new_user = False
        self.name = "filarty"

    def connected(self, ip: str, port: int) -> None:
        self.sock.connect((ip, port))
        self.main_window()

    def login(self):
        login = InputLogin()
        client.name = login.main()
        self.sock.send(Protocol.login(self.name).encode())

    def send_message(self, message: str):
        protocol_json = Protocol.message(self.name, message)
        self.sock.send(protocol_json.encode())

    def get_message(self):
        while True:
            message = self.sock.recv(2024)
            message = Protocol.decode_json(message)

            if "send" in message[0]:
                self.update_Text(message)

            if "add" in message[0]:
                self.new_user = True
                self.users = message[0]["add"]

    def users_update(self):
        if self.new_user:
            self.__window["users"].update(self.users)
            self.new_user = False

    def create_window(self):
        layout = [
            [self.pg.Text("Main Chat"),
             self.pg.Text("Users", justification="right", pad=((275, 0), (0, 0)))],
            [self.pg.Multiline(k="multi", disabled=True, size=(45, 27)),
             self.pg.Listbox(values=[], size=(20, 25), k="users")],
            [self.pg.InputText(k="message", size=(37, 30), font=20, expand_y=True, ),
             self.pg.Button("Send", bind_return_key=True, font=10, size=(30, 30))]
        ]
        window = pg.Window("Chat v1.0", layout, size=(500, 550))
        return window

    def update_Text(self, message):
        result = message[0]['send']
        self.__window["multi"].print(f"{result['time']} {result['user']} -> {result['message']}")

    def main_window(self):
        self.login()
        t = Thread(target=self.get_message, daemon=True)
        t.start()
        self.__window = self.create_window()
        while True:
            event, count = self.__window.read(timeout=1000)
            self.users_update()
            if event == pg.WIN_CLOSED:
                break
            if event == "Send":
                self.__window["message"].update("")
                self.send_message(count["message"])

        self.sock.close()
        self.__window.close()


if __name__ == "__main__":
    client = Client(pg)
    client.connected("localhost", 51007)
