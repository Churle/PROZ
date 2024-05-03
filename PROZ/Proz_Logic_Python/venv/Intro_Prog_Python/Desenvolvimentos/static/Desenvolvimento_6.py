print("Bem vindo usuario")
programa = True

while (programa):
  try:
# Captura de nome
    nome = input("Digite seu nome: ")

# Verificação do nome (se contém algum número)
    if any(char.isdigit() for char in nome):
      raise ValueError("Nome inválido. Não deve conter números.")

      print("Seu nome:", nome)

  #captacao de idade :

    idade=int(input("Digite sua idade "))
    print("Sua idade :",idade)
    
  #verificacao da idade

    if not isinstance (idade,int) or idade <=0:
      print("Voce digitou uma idade inexistente tente novamente ")
      continue
    
    
  #Verificacao de dada de nascimento:

    data=int(input("Digite seu ano de nascimento (Valido apenas 1922 a 2021) "))
    print("Ano de nascimento: ",data)

  #Verificacao da data de nascimento

    if not isinstance(data,int) or data < 1920 or data > 2024:
      print("Voce digitou uma entrada invalida ")
      continue
    
    Prox_Ano = 2025
    Data_Atual =  (Prox_Ano - data)
    print(nome," sua idade em 2022 sera: ", Data_Atual)

  except(ValueError,TypeError):
    print("Entrada invalida")

#calc_data()