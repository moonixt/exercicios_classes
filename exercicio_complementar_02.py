class Veiculo:
    def __init__(self, marca: str, modelo: str, rodas: int, velocidade: int = 0):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = velocidade

    def acelerar(self, valor):
        self.__velocidade = self.__velocidade + valor

    def frear(self, valor):
        self.__velocidade = self.__velocidade - valor

    def get_velocidade(self):
        return self.__velocidade


class Bicicleta(Veiculo):
    def __init__(self, marca: str, modelo: str, rodas: int,
                 marchas: int, bagageiro: bool, velocidade: int = 0):
        super().__init__(marca, modelo, rodas, velocidade)
        self.marchas = marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.marchas)
        print(self.bagageiro)


class Automovel(Veiculo):
    def __init__(self, marca: str, modelo: str, rodas: int, potencia: float, velocidade: int = 0):
        super().__init__(marca, modelo, rodas, velocidade)
        self.potencia = potencia


class Carro(Automovel):
    def __init__(self, marca: str, modelo: str, rodas: int, potencia: float, portas: int,
                 velocidade: int = 0):
        super().__init__(marca, modelo, rodas, potencia, velocidade)
        self.portas = portas

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.potencia)
        print(self.portas)


class Moto(Automovel):
    def __init__(self, marca: str, modelo: str, rodas: int, potencia: float, partida_eletrica: bool,
                 velocidade: int = 0):
        super().__init__(marca, modelo, rodas, potencia, velocidade)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.potencia)
        print(self.partida_eletrica)


carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()   # imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()    # imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()    # imprime os valores de todos os atributos da moto

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15
