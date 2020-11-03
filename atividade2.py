variavel=" "
def parametroString():
    variavel=input("Insira os caracteres {[()]}: ")
    if "{[()]}" in variavel:
        print("Parâmetro ok!",True)
        return True
    elif "{[()()]}" in variavel:
        print("Parâmetro ok!",True)
        return True
    else:
        print("Algo deu errado...",False)
        return False
parametroString()