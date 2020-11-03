listaNumeros = [1,2,3,4]
numero=0
def rotacaoLista(lista, numero):
    numero=int(input("Insira um número positivo ou negativo: "))
    if numero >= 0:
        for i in range(numero):
            numeroFim = lista.pop(-1)
            lista.insert(0, numeroFim)
    else:
        for i in range(abs(numero)):
            numeroInicio = lista.pop(0)
            lista.append(numeroInicio)
            return
rotacaoLista(listaNumeros, numero)
print (listaNumeros) #[1, 2, 3, 4, 5, 6]
    



       




