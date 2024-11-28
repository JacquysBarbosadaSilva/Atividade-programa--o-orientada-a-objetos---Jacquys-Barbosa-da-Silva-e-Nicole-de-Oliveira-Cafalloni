# Jacquys Barbosa da Silva e Nicole de Oliveira Cafalloni
from main import Cliente, Conta # importa as classes cliente e conta do main


print("======================================")
login_cadastrar = input("Voce ja tem uma conta? Digite sim ou nao\n") 
print("======================================")

if login_cadastrar.lower() == "nao":

    user_conta = input("Digite o nome do proprietário da conta: ")
    password = input("Digite a senha do proprietário da conta: ")
    saldo_user = input("Digite o saldo do proprietário da conta: ")
    print("======================================") 

    cadastro_user = Cliente(user_conta, password, saldo_user)

    conta_user = Conta(cadastro_user.nome, cadastro_user.saldo)

else:
    print("======================================")
    print("Operação em andamento")
    print("======================================")