import socket
import asyncio
from JsonProtocol import Protocol


class Server:
    def __init__(self, ip: str, port: int) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.users = []
        self.loop = asyncio.get_event_loop()

    def start(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen()
        self.loop.run_until_complete(self.main())

    async def send_all_message(self, message: bytes):
        for user in self.users:
            await self.loop.sock_sendall(user, message)

    async def accept_connection(self):
        while True:
            sock, ip = await self.loop.sock_accept(self.socket)
            print(f" {ip} has connected")
            self.users.append(sock)
            self.loop.create_task(self.get_message(sock))

    async def get_message(self, sock: socket):
        while True:
            try:
                message = await self.loop.sock_recv(sock, 2024)
                await self.send_all_message(message)
                json_message = Protocol.decode_json(message)
                print(json_message[0]["send"])
            except:
                self.users.remove(sock)
                break

    async def main(self):
        await asyncio.gather(self.accept_connection())


if __name__ == "__main__":
    server = Server("localhost", 54007)
    server.start()
