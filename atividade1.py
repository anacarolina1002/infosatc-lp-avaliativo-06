def verificaNumero():
    listaSec=[]
    lista = ["1","2","3","4"]
    numero=0
    numero = int(input("Insira um número INTEIRO (+ ou -): "))
    if numero < 0:
        listaSec.append(lista[numero]) 
        lista.pop(numero)
        listaSec=listaSec+lista
        print(listaSec)
           
    else: 
        listaSec=[]
        listaSec.append(lista[numero]) 
        lista.pop(numero)
        listaSec=lista+listaSec
        print(listaSec)
verificaNumero()



       




