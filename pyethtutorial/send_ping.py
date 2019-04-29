from discovery import EndPoint, Server, Node
import binascii

# don't need
bootnode_key = ""

# BootNode info
bootnode_endpoint = EndPoint(u'127.0.0.1', 30303, 30303)
bootnode = Node(bootnode_endpoint, binascii.a2b_hex(bootnode_key))

# My endpoint info
my_endpoint = EndPoint(u'127.0.0.1', 30304, 30304)
server = Server(my_endpoint, bootnode)

listen_thread = server.listen_thread()
listen_thread.start()

discover_thread = server.discover_thread()
discover_thread.start()

listen_thread.join()
discover_thread.join()
