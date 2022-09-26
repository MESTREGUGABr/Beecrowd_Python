loop = int(input())
for laco in range(loop):
    b,e = map(int,input().split())
    ida_inicio=''
    espelho=''
    #A ideia é receber a ordenação dos valores, e converter elas para uma string. Para inverter facilmente depois com o método de fatiar
    while b <= e:
        ida_inicio+=str(b)
        b+=1
    # depois de ter convertido para "string", peguei a string e inverti imprimindo 
    espelho = ida_inicio+ida_inicio[::-1]
    print(espelho)