#Plug 1
p1,p2,p3,p4,p5 = map(int,input().split())
#Plus2 
t1,t2,t3,t4,t5 = map(int,input().split())
if ((p1 == 0 and t1 == 1) or (p1 == 1 and t1 == 0)) and ((p2 == 0 and t2 == 1) or (p2 == 1 and t2 == 0)) and ((p3 == 0 and t3 == 1) or (p3 == 1 and t3 == 0)) and ((p4 == 0 and t4 == 1) or (p4 == 1 and t4 == 0)) and ((p5 == 0 and t5 == 1) or (p5 == 1 and t5 == 0)):
    print('Y')
else: 
    print('N')