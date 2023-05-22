def add(a,b):
    answer=a+b
    print(answer,'\n')
def sub(a,b):
    answer=a-b
    print(answer,'\n')
def div(a,b):
    answer=a/b
    print(answer,'\n')
def mul(a,b):
    answer=a*b
    print(answer,'\n')

while True:
    print('A.Addition')
    print('B.subtraction')
    print('C.division')
    print('D.multiplication')
    print('E.exit')
    
    choice=input('enter')
    if choice=='A' or choice=='a' :
        print('addition')
        a=int(input())
        b=int(input())
        add(a,b)
    elif choice=='B' or choice=='b' :
        print('subtraction')
        a=int(input())
        b=int(input())
        sub(a,b)
    elif choice=='C' or choice=='c' :
        print('division')
        a=int(input())
        b=int(input())
        div(a,b)
    elif choice=='D' or choice=='d':
        print('multiplication')
        a=int(input())
        b=int(input())
        mul(a,b)
    elif choice=='E' or choice=='e':
        print('quite')
        break     
