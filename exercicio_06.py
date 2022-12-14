class Veiculo:
    def __init__(self,ano:str, preco:float, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print(self.ano)
        print(self.preco)

class Motor:
    def __init__(self,cilindrada:int, potencia:int):
        self.cilindrada = cilindrada
        self.potencia = potencia

class Carro(Veiculo):
    def __init__(self,ano:str, preco:float, motor, cor:str, modelo:str):
        super().__init__(ano,preco,motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        super().exibir_dados()
        print(self.cor)
        print(self.modelo)

class Caminhao(Veiculo):
    def __init__(self, ano:str, preco:float, motor, comprimento:float):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        super().exibir_dados()
        print(self.comprimento)

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()        # imprime os valores de todos os atributos do caminhão
