a = 4
b = 3

op="+"

if op=="+":
    print(a+b)
elif op=="-":
    print("a-b")
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("Operador inválido")
    
clima="sol"
dinheiro = 650
lugar=""

if clima=="sol" or dinheiro >= 300 and dinheiro<=500:
    lugar="clube"
else:
    lugar="cinema"
    
print("vou ao " + lugar)
