listaNumeros = [1,2,3,4]#declaração das coisinhas do programa
numero=0
def rotacaoLista(lista, numero):#definição de uma def com dois argumentos
    numero=int(input("Insira um número positivo ou negativo: "))
    if numero >= 0:
        for i in range(numero):
            numeroFim = lista.pop(-1)#nessa parte, se um número é positivo, ele decremente o número final e adiciona ele no começo
            lista.insert(0, numeroFim)#no começo, na posição 0, no caso.
    else:
        for i in range(abs(numero)):
            numeroInicio = lista.pop(0)#aqui ele decrementa do início e adiciona no final.
            lista.append(numeroInicio)
            return
rotacaoLista(listaNumeros, numero)#Inicia o programa
print (listaNumeros) #[1, 2, 3, 4, 5, 6]
    



       




