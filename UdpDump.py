from tabulate import tabulate


class UdpDump:
    def __init__(self, session):
        self._table = []
        self.session = session
        self.tcp_items = session.walk('.1.3.6.1.2.1.7.5.1.1')
        self.transformDataFromOID()

    def transformDataFromOID(self):
        for item in self.tcp_items:
            aux = item.oid_index.split(".")

            ip_local = '.'.join(aux[:4])
            porta_local = aux[4]

            self._table.append(['udp', ip_local, porta_local])

    # Usa a biblioteca tabulate para printar na tela o resultado.
    def print_table(self):
        print(tabulate(
            self._table,
            headers=['Protocolo', 'ip local', 'porta (local)']
        ))
