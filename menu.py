# Jacquys Barbosa da Silva e Nicole de Oliveira Cafalloni

from cadastro import conta_user

while True:

    print("======================================")
    print("Digite o que deseja fazer\n1 - sacar\n2 - depositar\n3 - extrato\n4 - historico\n5 - sair")
    escolha = int(input())
    print("======================================")

    match escolha:
        case 1:
            valor = float(input("Digite o valor que deseja sacar: "))
            conta_user.sacar(valor)
        
        case 2:
            valor = float(input("Digite o valor que deseja depositar: "))
            conta_user.depositar(valor)
        
        case 3:
            conta_user.extrato()
        
        case 4:
            conta_user.historico_transacoes()

        case 5:
            print("\n======================================\n")
            print("Saindo...")
            print("\n======================================\n")
            break