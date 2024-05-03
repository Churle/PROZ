import random

def sistema_loja():
  loja = True

  while loja:
    produtos =['Games','consoles','controles','headset','cadeiras']    
    print('Bem vindo a loja, escolha um produto de indice 0 a 4 para conferir a disponibilidade')
    print("total de produtos = ",len(produtos))
    print("Lista produtos 0 a 4 : ",produtos)
    for i in range(len(produtos)):
     print("lista produtos em coluna : ",produtos[i])
    
    ind = int(input("Indice = ?"))


    if ind < 0 or ind > 4:
      aleatorio = random.randint(0,len(produtos)-1)
      print("Indice Inexistente tente novamente")
      print("Exemplo randomico de produto: ", produtos[aleatorio])
      continue
    
    elif print("Temos o produto ", produtos[ind], " a venda!"):
      loja = False
    break

sistema_loja()