from pystyle import *

print(Box.Lines("culcolater"))
Write.Print('wolcame to calcolator \n',Colors.blue_to_green,interval=0.2)
print(Box.DoubleCube('last go'))

while True:
    num1=int(Write.Input('input your first number : \n' ,Colors.black_to_green,interval=0.1))

    opr=Write.Input('input your operetor : ',Colors.black_to_white)
   
    num2=int(Write.Input('input your scaund number : \n' ,Colors.black_to_green,interval=0.1))

    if opr== '+':
        Write.Print('the asnwer is :',Colors.blue_to_purple,interval=0.1,)
        print(num1+num2)
        break
    elif opr=='-':
        Write.Print('the asnwer is :',Colors.blue_to_purple,interval=0.1,)
        print(num1-num2)
        break
    elif opr=="*":
        Write.Print('the asnwer is :',Colors.blue_to_purple,interval=0.1,)
        print(num1*num2)
        break
    elif opr=="/":
        Write.Print('the asnwer is :',Colors.blue_to_purple,interval=0.1,)
        print(num1/num2)
        break
    else:
      Write.Print('oops you missing yor operetor :',Colors.blue_to_purple,interval=0.1,)
    