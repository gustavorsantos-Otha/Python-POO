# declaração de classe
class Pessoa:
    def __init__(self): # método construtor
    #atributos de instância
        self.nome = ""
        self.idade = 0
        
    #métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"
#declaração de objetos

p1 = Pessoa()
p1.nome = "Maria"
p1.idade = 18
p1.aniversario()
print(p1.mensagem())
