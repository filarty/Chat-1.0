import socket
import asyncio


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

    async def accept_connection(self):
        while True:
            sock, ip = await self.loop.sock_accept(self.socket)
            print(f" {ip} has connected")
            self.users.append(sock)
            self.loop.create_task(self.get_message(sock))

    async def get_message(self, sock: socket):
        while True:
            message = await self.loop.sock_recv(sock, 2024)
            print(message.decode())

    async def main(self):
        await asyncio.gather(self.accept_connection())


if __name__ == "__main__":
    server = Server("localhost", 52007)
    server.start()
