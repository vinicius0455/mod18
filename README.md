# mod18
1. Exceções personalizadas
ProdutoInexistenteError, QuantidadeInvalidaError, SaldoInsuficienteError, CarrinhoVazioError: usadas para lidar com erros específicos durante as interações do usuário.

2. Dados iniciais
produtos: dicionário com itens disponíveis e seus preços.

carrinho: dicionário para armazenar os produtos adicionados.

saldo: valor de dinheiro disponível para o pagamento.

3. Funções principais
mostrar_produtos(): lista os produtos disponíveis.

adicionar_ao_carrinho(): permite escolher um produto e a quantidade desejada. Valida a entrada e adiciona ao carrinho.

ver_total(): calcula e exibe o valor total dos produtos no carrinho.

simular_pagamento(): tenta realizar o pagamento. Verifica se o carrinho não está vazio e se há saldo suficiente. Em caso de sucesso, desconta o valor do saldo e limpa o carrinho.

menu(): apresenta opções ao usuário em um loop contínuo até que ele escolha sair.

4. Menu de opções
Permite ao usuário:
Ver produtos
Adicionar ao carrinho
Ver total da compra
Pagar
Ver saldo
Sair
