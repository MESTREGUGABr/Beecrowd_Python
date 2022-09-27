(comprimento_estrada,dist_pedagio) = [int(x) for x in input().split()]
(custo_km,valor_pedagio) = [int(x) for x in input().split()]

custo_viagem = comprimento_estrada*custo_km
qnt_pedagios = int(comprimento_estrada/dist_pedagio)


total = custo_viagem + (qnt_pedagios*valor_pedagio)
print(int(total))