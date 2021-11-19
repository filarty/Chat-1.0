
import PySimpleGUI as pg


colors = ["#F04D0B", "#96F109", "#09EDF1", "#F109F1", "#F10909"]


class MainWindow:
    def __init__(self, pg: pg) -> None:
        self.pg = pg
        self.__window = None

    def create_window(self):
        layout = [
            [self.pg.Text("Main Chat"),
             self.pg.Text("Users", justification="right", pad=((275, 0), (0, 0)))],
            [self.pg.Multiline(k="multi", disabled=True, size=(45, 27)),
             self.pg.Listbox(values=["name1", "name2", "name3"], size=(20, 25))],
            [self.pg.InputText(k="message", size=(37, 30), font=20, expand_y=True, ),
             self.pg.Button("Send", bind_return_key=True, font=10, size=(30, 30))]
        ]
        window = pg.Window("Chat v1.0", layout, size=(500, 550))
        return window

    def update_Text(self, message: str):
        self.__window["multi"].print(message)
        self.__window["message"].update("")

    def main(self):
        self.__window = self.create_window()
        while True:
            event, count = self.__window.read(timeout=1000)
            if event == pg.WIN_CLOSED:
                break
            if event == "Send":
                self.update_Text(count["message"])
        self.__window.close()


if __name__ == "__main__":
    window = MainWindow(pg)
    window.main()
