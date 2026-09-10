class Agendamento:
    # Variável do ID inicia como None:
    id = None

    # Construtor:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status):
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    # Métodos:
    def exibir(self):
        return (f"Cliente: {self.cliente}  |  Telefone: {self.telefone}  |  Serviço: {self.servico}  |  Preço: {self.preco}  |  "
                f"Barbeiro: {self.barbeiro}  |  Data: {self.data}  |  Horário: {self.horario}  |  Status: {self.status}")

    def converte_tupla(self):
        return (self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        objeto = Agendamento(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8])
        objeto.id = tupla[0]
        return objeto