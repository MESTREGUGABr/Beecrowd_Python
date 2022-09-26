diam_boliche = int(input())
alt,larg,prof = map(int,input().split(' '))

if diam_boliche <= alt and diam_boliche <= larg and diam_boliche <= prof:
    print('S')
else:
    print('N')