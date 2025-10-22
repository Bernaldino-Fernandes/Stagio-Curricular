#                           Exercicios Parte 1
# Primeiro criamos a funcao onde vai conter toda a logica
def listaNum():
    #Lista contendo os numeros
    try:
        entrada = input("Escreva uma lista de numeros inteiros separados por virgulas: ")
        lista = [int(x)for x in entrada.split(",")]
        
        if all(isinstance(x,(int,float))for x in lista):

            # Todos Os dados pedidos no enunciado
            listaOrdenada = sorted(lista)
            MaiorNum = max(lista)
            menorNum = min(lista)
            media = sum(lista)/len(lista)

            # Impressao dos resultados
            print("Lista ordenada de forma crescente: ", listaOrdenada)
            print("O maior numero é: ", MaiorNum)
            print("O menor numero é: ", menorNum)
            print("A media entre os numeros da lista é: ", media)
        else:
            print("A lista contem letras, refaca e coloque somente numeros!")
            print(lista)
    except:
        print("Digit somente numeros!")
# Aqui chamamos a funcao contendo toda a lógica 

listaNum()
