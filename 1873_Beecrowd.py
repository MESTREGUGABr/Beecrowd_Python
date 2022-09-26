qnt = int(input())
for loop in range(qnt):
    jogada1, jogada2 = input().split()

    if jogada1 == 'tesoura' and jogada2 == 'tesoura':
        print('empate')
    elif jogada1 == 'papel' and jogada2 == 'papel':
        print('empate')
    elif jogada1 == 'spock' and jogada2 == 'spock':
        print('empate')
    elif jogada1 == 'lagarto' and jogada2 == 'lagarto':
        print('empate')
    elif jogada1 == 'pedra' and jogada2 == 'pedra':
        print('empate')

    elif jogada1 == 'tesoura' and jogada2 == 'papel':
        print('rajesh')
    elif jogada1 == 'papel' and jogada2 == 'pedra':
        print('rajesh')
    elif jogada1 == 'papel' and jogada2 == 'lagarto':
        print('rajesh')
    elif jogada1 == 'lagarto' and jogada2 == 'spock':
        print('rajesh')
    elif jogada1 == 'spock' and jogada2 == 'tesoura':
        print('rajesh')
    elif jogada1 == 'tesoura' and jogada2 == 'lagarto':
        print('rajesh')
    elif jogada1 == 'lagarto' and jogada2 == 'papel':
        print('rajesh')
    elif jogada1 == 'papel' and jogada2 == 'spock':
        print('rajesh')
    elif jogada1 == 'spock' and jogada2 == 'pedra':
        print('rajesh')
    elif jogada1 == 'pedra' and jogada2 == 'tesoura':
        print('rajesh')

    elif jogada1 == 'papel' and jogada2 == 'tesoura':
        print('sheldon')
    elif jogada1 == 'pedra' and jogada2 == 'papel':
        print('sheldon')
    elif jogada1 == 'lagarto' and jogada2 == 'papel':
        print('sheldon')
    elif jogada1 == 'spock' and jogada2 == 'lagarto':
        print('sheldon')
    elif jogada1 == 'tesoura' and jogada2 == 'spock':
        print('sheldon')
    elif jogada1 == 'lagarto' and jogada2 == 'tesoura':
        print('sheldon')
    elif jogada1 == 'papel' and jogada2 == 'lagarto':
        print('sheldon')
    elif jogada1 == 'spock' and jogada2 == 'papel':
        print('sheldon')
    elif jogada1 == 'pedra' and jogada2 == 'spock':
        print('sheldon')
    elif jogada1 == 'tesoura' and jogada2 == 'pedra':
        print('sheldon')

