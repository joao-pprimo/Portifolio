#Construtores e self
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

# Métodos
class Conta:
    def __init__(self, numero, cpf,nomeTitular, saldo):
         self.numero = numero
         self.cpf = cpf
         self.nomeTitular = nomeTitular
         self.saldo = saldo
    def depositar(self, valor):
         self.saldo += valor
    def sacar(self, valor):
         self.saldo -= valor
# Métodos com Retorno
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")


def main():
    c1 = Conta(1, 1, "Joao", 0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")


if __name__ == "__main__":
    main()
# Objetos na memória
class Conta:
   def __init__(self, numero, cpf,    nomeTitular, saldo):
      self.numero = numero
      self.cpf = cpf
      self.nomeTitular = nomeTitular
      self.saldo = saldo
   def depositar(self, valor):
      self.saldo += valor
   def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         return True
def gerarextrato(self):
        print(f"numero:{self.numero}\n     cpf:{self.cpf}\nsaldo:{selfsaldo}")
def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
           return ("Não existe saldo suficiente")
        else:
           contaDestino.depositar(valor)
           self.saldo -= valor
        return ("Transferencia Realizada")