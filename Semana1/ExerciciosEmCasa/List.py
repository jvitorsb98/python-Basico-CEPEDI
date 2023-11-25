carros = ["HRV","Golf","Argo","Focus"]

carros.append("Fit")
carros.append("Fox")

carros.remove("Focus")
carros.pop()

print(carros)

carros2 = list(carros)

carros.append("cacau")

carros3 = carros2+carros;


carros.clear()

print(str(len(carros3)))
print(carros2)