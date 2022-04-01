n1 = float(input("Coloque o primeiro nunero: "))
n2 = float(input("Coloque o segundo numero: "))

print('-'* 35)

print("Numeros Escolhidos: ",(n1) + (n2))

print("-" *35)

e = input("que operaçao voce deseja fazer? \n(1)adiçao \n(2)subtraçao \n(3)Divisão \n(4)Multiplicaçao \n")

if(e == "1"):
    e=n1+n2
    print("-")
    print("Resultado: ",(e))
    
elif(e == "2"):
    e=n1-n2
    print("-"*35)
    print("Resultado: ",(e))
    
elif(e == "3"):
    e=n1/n2
    print("-"*35)
    print("Resultado: ",(e))
    
elif(e == "4"):
    e=n1*n2
    print("-"*35)
    print("Resultado: ",(e))
    
else:
    print("Digite uma opçao valida")

    