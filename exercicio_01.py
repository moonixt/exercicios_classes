class Pessoa:
    def __init__ (self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir(self):
        print(self.nome)
        print(self.idade)
        print(self.cpf)
        

class Aluno(Pessoa):
    def __init__(self,nome,idade,cpf,ra,turma):
        super().__init__(nome,idade,cpf)
        self.ra = ra
        self.turma = turma

    def exibir(self):
        super().exibir()
        print(self.ra)
        print(self.turma)

class Professor(Pessoa):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf)
        self.salario = salario 

    def exibir(self):
        super().exibir()
        print(self.salario)
        

aluno1 = Aluno('Paulo', 26, '23232323', 32323232, 'SI2A',)
professor1 = Professor('Paulo', 26, '23232323', 'R$5000')

professor1.exibir()

aluno1.exibir()