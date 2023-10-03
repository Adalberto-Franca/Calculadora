def menu():
    print('=================CALCULADORA=================\n')
    print('Digite 1 para soma.\n')
    print('---------------------------------------------')
    print('Digite 2 para subtração.\n')
    print('---------------------------------------------')
    print('Digite 3 para multiplicação.\n')
    print('---------------------------------------------')
    print('Digite 4 para divisão.\n')
    print('---------------------------------------------')
    op = int(input('Digite 5 para sair da calculadora.\n'))
    print('---------------------------------------------')
    return op

def calcular():
    x = int(input('Digite o valor X: '))
    y = int(input('Digite o valor y: '))
    print('-------------------------------\n')
    return x, y

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

resultados = []
op = 0
while op != 5:
    op = menu()
    if op == 1:
        x,y = calcular()
        r = soma(x, y)
        resultados.append(r)
        print(f'O resultado da soma é: ',r,'\n')

    elif op == 2:
        x,y = calcular()
        r = sub(x,y)
        resultados.append(r)
        print(f'O resultado da subtração é: ',r,'\n')

    elif op == 3:
        x,y = calcular()
        r = mult(x,y)
        resultados.append(r)
        print(f'O resultado da multiplicação é: ',r,'\n')

    elif op == 4:
        x,y = calcular()
        r = div(x,y)
        resultados.append(r)
        print(f'O resultado da divisão é: ',r,'\n')

    elif op == 5:
        pass
        print (f'==========VOLTE SEMPRE==========\n')
    else:
        print (f'==========OPÇÃO INVALIDA==========\n')

aux=1
for i in resultados:
    print ("O valor da",aux,"° posicao é: ",i)
    aux+=1