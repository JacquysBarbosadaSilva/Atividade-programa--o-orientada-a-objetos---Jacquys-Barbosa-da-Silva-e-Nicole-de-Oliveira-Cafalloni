# Jacquys Barbosa da Silva e Nicole de Oliveira Cafalloni
from datetime import datetime
data_hora = datetime.today().strftime("%Y-%m-%d %H:%M")


class Cliente:

    def __init__(self, nome, senha, saldo):

        self.nome = nome
        self.senha = senha
        self.saldo = float(saldo)
        print (f"\n======================================\nUsuário cadastrado com sucesso\n======================================\n")

class Conta:

    def __init__(self, titular, saldo_inicial):

        self.titular = titular
        self.saldo = float(saldo_inicial)
        self.historico = [
            f"Conta criada em {datetime.today().strftime('%Y-%m-%d %H:%M')} com saldo inicial de R$ {self.saldo:.2f}"
        ]

    def sacar(self, valor):
        if valor < 0:
            print("\n======================================\nValor inválido!\n======================================")
        elif valor > self.saldo:
            print("\n======================================\nSaldo insuficiente!\n======================================")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque de R$ {valor:.2f} em {datetime.today().strftime('%Y-%m-%d %H:%M')}")
            print(f"\n======================================\nSaque no valor de R$ {valor:.2f} foi realizado\n======================================\nSaldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor < 0:
            print("\n======================================\nValor inválido!\n======================================")
            
        else:
            self.saldo += valor
            self.historico.append(f"Depósito de R$ {valor:.2f} em {datetime.today().strftime('%Y-%m-%d %H:%M')}")
            print(f"\n======================================\nDepósito no valor de {valor:.2f} foi realizado\n======================================\nSaldo atual: R$ {self.saldo:.2f}")

    def extrato(self):
        print("\n======================================\n") 
        print("==========Extrato da conta==========")
        print(f"Titular da conta: {self.titular}")   
        print(f"Saldo da conta: {self.saldo:.2f}")
        print(f"Extrato realizado em {data_hora}")
        print("======================================\n") 

    def historico_transacoes(self):
        print("\n======================================\n")
        print("Histórico de transações:")
        for transacao in self.historico:
            print(f"{transacao}")
        print("\n======================================\n")


