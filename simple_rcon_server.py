from rcon_server.rcon_server import RCONServer
from rcon_server.rcon_packet import RCONPacket
import asyncio

test_password = "changeme"
test_bind = ("0.0.0.0",27015)

class DummyRCONServer(RCONServer):

    def __init__(self):
        super().__init__(bind=test_bind ,password=test_password)

    def handle_execcommand(self, packet, connection):
        response = RCONPacket(packet.id,
                              RCONPacket.SERVERDATA_RESPONSE_VALUE,
                              packet.body)
        connection.send_packet(response)


# Entry point for the script
if __name__ == "__main__":
    rcon_server = DummyRCONServer()
    
    asyncio.run(rcon_server.listen())