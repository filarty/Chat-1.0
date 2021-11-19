import socket
import asyncio


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.loop = asyncio.get_event_loop()

    def connected(self, ip: str, port: int) -> None:
        self.sock.connect((ip, port))
        self.loop.run_until_complete(self.main())

    async def send_message(self):
        while True:
            message = await self.loop.run_in_executor(None, input, "send message: ")
            await self.loop.sock_sendall(self.sock, message.encode())

    async def get_message(self):
        while True:
            message = await self.loop.sock_recv(self.sock, 2024)
            print(message.decode())

    async def main(self):
        await asyncio.gather(self.send_message(), self.get_message())


if __name__ == "__main__":
    client = Client()
    client.connected("localhost", 52007)
