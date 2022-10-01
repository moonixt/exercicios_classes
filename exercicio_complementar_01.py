class Pessoa:
    def __init__(self, nome: str, endereco: str, fone: str, cpf: str):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self, nome: str, endereco: str, fone: str, cpf: str, disciplina: list = []):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = disciplina

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Disciplina:
    def __init__(self, nome: str):
        self.nome = nome


class Funcionario(Pessoa):
    def __init__(self, nome: str, endereco: str, fone: str, cpf: str, salario: float):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Professor(Funcionario):
    def __init__(self, nome: str, endereco: str, fone: str, cpf: str, salario: float,
                 titulacao: str, disciplina: list = []):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplina = disciplina

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Tecnico(Funcionario):
    def __init__(self, nome: str, endereco: str, fone: str, cpf: str, salario: float, cargo: str):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo


disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456", "(11)99999-9555", "9999999",
                       2000, "Mestrado")


aluno1 = Aluno("Maria", "Avenida São Francisco, 239",
               "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77",
                   "(11)93333-3333", "8787887", 1500, "Tecnico")

aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)

print('Disciplinas associadas ao aluno:')
for d in aluno1.disciplina:
    print(d.nome)

print('Disciplinas associadas ao Professor:')
for d in professor1.disciplina:
    print(d.nome)
