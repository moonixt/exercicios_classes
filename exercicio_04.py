class Animal:
    def __init__(self, nome:str, cor:str, numero_patas: int):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print(self.nome)
        print(self.cor)
        print(self.numero_patas)

class Cachorro(Animal):
    def __init__ (self,nome:str, cor:str, numero_patas:int, raca:str):
        super().__init__(nome,cor,numero_patas)
        self.raca = raca

    def exibir_dados(self):
        super().exibir_dados()
        print('Raça: ',self.raca)

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()          # exibe os atributos do cachorro