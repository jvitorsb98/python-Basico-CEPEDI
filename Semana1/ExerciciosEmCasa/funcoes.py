def somar(*n):
    r = 0
    for x in n:
        r += x
    return r

def concatena (*t):
    r = ""
    for x in t:
        r += " " + x
    
    return r    
    
def carros(c):
    print("Modelo : " + c)
    
carros("HRV")

result = somar(1,2,3,4,5,6,9)
print(result)

texto = concatena("uma","coisa","engraçada")
print(texto)
