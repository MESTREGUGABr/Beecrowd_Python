caracter = input()
texto = input().split()
#Usarei um contador que começa em 0, para fazer a porcentagem de palavras que contém a letra 
cont = 0. 
# usarei um for para percorrer o texto digitado
for corre in texto:
    if caracter in corre:
        cont = cont +1 
cont /= len(texto)/100
#Tive que pesquisar essa forma de exibição, mas imprimindo a % do cont com uma casa 
print('%.1f' % cont)