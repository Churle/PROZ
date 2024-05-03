def calculadora(num1, num2, entrada):
    while True:  # Loop infinito
        if entrada == 1:
            resultado = float(num1) + float(num2)
            return resultado
        elif entrada == 2:
            resultado = float(num1) - float(num2)
            return resultado
        elif entrada == 3:
            resultado = float(num1) / float(num2)
            return resultado
        elif entrada == 4:
            resultado = float(num1) * float(num2)
            return resultado
        elif entrada == 5:
            print("Saida Confirmada")
            return None
        else:
            print("Você digitou um número inválido.")
        
        # Se a execução chegar aqui, pede uma nova entrada
        entrada = float(input("Digite 1 para somar, 2 para subtrair, 3 para dividir, 4 para multiplicar, 5 para sair: "))

# Testando a função
while True:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    entrada = float(input("Digite 1 para somar, 2 para subtrair, 3 para dividir, 4 para multiplicar, 5 para sair: "))

    result_calc = calculadora(a, b, entrada)
    
    if result_calc is not None:
        print("O resultado é:", result_calc)

    if entrada == 5:
        print("Encerrando o programa.")
        break  # Sair do loop quando o usuário digitar 5
