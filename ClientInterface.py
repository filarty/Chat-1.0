import PySimpleGUI as pg
from random import choice

colors = ["#F04D0B", "#96F109", "#09EDF1", "#F109F1", "#F10909"]


class MainWindow:
    def __init__(self, pg: pg) -> None:
        self.pg = pg
        self.__window = None
        self.__messages_counter = 0

    def create_window(self):
        layout = [
            [self.pg.Text(k="text0")],
            [self.pg.Text(k="text1")],
            [self.pg.Text(k="text2")],
            [self.pg.Text(k="text3")],
            [self.pg.Text(k="text4")],
            [self.pg.Text(k="text5")],
            [self.pg.Text()],
            [self.pg.Text()],
            [self.pg.InputText(k="message", size=5, font=5), self.pg.Button("Send", bind_return_key="Enter", font=5)]
        ]
        window = pg.Window("Chat v1.0", layout, size=(500, 500))
        return window

    def update_Text(self, message: str):
        if self.__messages_counter == 5:
            self.__messages_counter = 0
        counter = self.__messages_counter
        self.__window[f"text{counter}"].update(f"\n{message}", background_color=choice(colors))
        self.__window["message"].update("")
        self.__messages_counter += 1

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
