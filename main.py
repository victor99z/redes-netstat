from TcpDump import TcpDump
from UdpDump import UdpDump
from ConnSnmp import ConnSnmp
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        conn = ConnSnmp()
        print()
        tcp = TcpDump(conn.session)
        tcp.print_table()
        print()
        udp = UdpDump(conn.session)
        udp.print_table()
    elif len(sys.argv) == 2 and len(sys.argv[1]) >= 9:  # 127.0.0.0 ou localhost
        conn = ConnSnmp(sys.argv[1])
        print()
        tcp = TcpDump(conn.session)
        tcp.print_table()
        print()
        udp = UdpDump(conn.session)
        udp.print_table()
    elif len(sys.argv) == 3 and sys.argv[2] == '--udp':
        conn = ConnSnmp(sys.argv[1])
        print()
        udp = UdpDump(conn.session)
        udp.print_table()
    elif len(sys.argv) == 3 and sys.argv[2] == '--tcp':
        conn = ConnSnmp(sys.argv[1])
        print()
        tcp = TcpDump(conn.session)
        tcp.print_table()
    elif len(sys.argv) == 2 and sys.argv[1] == "--udp":
        conn = ConnSnmp()
        print()
        udp = UdpDump(conn.session)
        udp.print_table()
    elif len(sys.argv) == 2 and sys.argv[1] == "--tcp":
        conn = ConnSnmp()
        print()
        tcp = TcpDump(conn.session)
        tcp.print_table()
