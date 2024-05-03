#A loja Dessa vez, precisa que você atualize o array de produtos.
#Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.
#Como desafio, adicione dois novos produtos da sua escolha à lista. 

def loja_games():

  loja = True
  print("Bem vindo ao menu da loja, digite o numero referente a acao que deseja executar = Adicionar (1) / Remover (2) / Sair (3) ")
  produtos = ['Games', 'consoles', 'controles', 'headset', 'cadeiras']

  for i in range(len(produtos)):
    print("lista produtos:", produtos[i])


  while loja:
    numero =int(input("digite a opcao numerica: "))

    match numero:
      case 1:
        print("voce escolheu a opcao de adicionar um item a lista")
        new_produto =str(input("Didigite o produto que desejaadicionar"))
        produtos.append(new_produto)
        print(produtos)
        continue

      case 2:
        print("voce escolheu a opcao de remover um item da lista, veja a lista e decida qual item remover")
        print(produtos)
        kick_produto =str(input("Digite o nome do produto para remove-lo"))
        produtos.remove(kick_produto) 
        continue

      case 3:
        print("Voce escolheu sair ")
        loja = False
        break

      case _ if numero < 1 or numero > 3:
            print("Número inválido. Digite um número entre 1 e 3.")
            numero = int(input("Digite um número válido: "))
            continue

loja_games()