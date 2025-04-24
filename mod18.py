class ProdutoInexistenteError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class CarrinhoVazioError(Exception):
    pass

produtos = {
    "arroz": 2.50,
    "banana": 1.80,
    "leite": 3.00,
}

carrinho = {}
saldo = 30.00

def mostrar_produtos():
    print("\nProdutos Disponíveis")
    for nome, preco in produtos.items():
        print(f"{nome.title()} - €{preco:.2f}")
    print()

def adicionar_ao_carrinho():
    try:
        produto = input("Digite o nome do produto: ").strip().lower()
        if produto not in produtos:
            raise ProdutoInexistenteError("Produto não encontrado.")

        quantidade = input("Quantidade: ")
        if not quantidade.isdigit() or int(quantidade) <= 0:
            raise QuantidadeInvalidaError("Quantidade inválida.")

        quantidade = int(quantidade)
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade

        print(f"{quantidade} x {produto} adicionado ao carrinho.")
    except (ProdutoInexistenteError, QuantidadeInvalidaError) as e:
        print(f"Erro: {e}")
    except Exception:
        print("Erro")

def ver_total():
    total = sum(produtos[p] * q for p, q in carrinho.items())
    print(f"\nValor total da compra: €{total:.2f}")
    return total

def simular_pagamento():
    global saldo
    try:
        if not carrinho:
            raise CarrinhoVazioError("Carrinho está vazio.")

        total = ver_total()

        if total > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")

        saldo -= total
        print(f"\nPagamento realizado com sucesso")
        print(f"Valor pago: €{total:.2f}")
        print(f"Saldo restante: €{saldo:.2f}")
        carrinho.clear()

    except (SaldoInsuficienteError, CarrinhoVazioError) as e:
        print(f"Erro: {e}")
    except Exception:
        print("Erro")

def menu():
    while True:
        print("1 - Visualizar produtos")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Ver total da compra")
        print("4 - Simular pagamento")
        print("5 - Ver saldo atual")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            mostrar_produtos()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            ver_total()
        elif opcao == "4":
            simular_pagamento()
        elif opcao == "5":
            print(f"\nSaldo atual: €{saldo:.2f}")
        elif opcao == "0":
            print("Saindo")
            break
        else:
            print("Opção inválida.")


menu()
