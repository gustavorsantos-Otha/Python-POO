# declaração de classe
class Pessoa:
    """
    Essa classe cria um objeto de uma pessoa com nome e idade.

    Para criar uma nova pessoa use
    variável = pessoa(nome, idade)
    """
    def __init__(self, nome = "", idade = 0):  # método construtor
        # atributos de instância
        self.nome = nome
        self.idade = idade

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome: {self.nome} ; idade: {self.idade}"
# declaração de objetos

p1 = Pessoa("Maria", 17)
p1.aniversario()
print(p1)
print(p1.__dict__) #attribute
print(p1.__getstate__()) #method
print(p1.__class__)

p2 = Pessoa("Mauro", 52)
print(p2)
print(p2.__dict__)
print(p2.__getstate__())

print(p1.__doc__) #DUNDER attribute
