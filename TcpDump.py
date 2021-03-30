from tabulate import tabulate


class TcpDump:
    def __init__(self, session):
        self._table = []
        self.session = session
        self.tcp_items = session.walk('.1.3.6.1.2.1.6.13.1.1')
        self.transformDataFromOID(self)
    
    # Faz um split pelo array resultante de tcp_items e coloca na tabela os valores para serem monstrados
    def transformDataFromOID(self, item):
        for item in self.tcp_items:
            aux = item.oid_index.split(".")

            if int(item.value) == 5:
                tipo = "ESTABLISHED"
                ip_local = '.'.join(aux[:4])
                porta_local = aux[4]
                ip_remoto = '.'.join(aux[5:9])
                porta_remota = aux[9]
                self._table.append(['tcp', ip_local, porta_local, ip_remoto, porta_remota, tipo])

    # Usa a biblioteca tabulate para printar na tela o resultado.
    def print_table(self):
        print(tabulate(
            self._table,
            headers=['Protocolo', 'ip local', 'porta (local)', 'ip remoto', 'porta (remoto)', 'estado']
        ))
