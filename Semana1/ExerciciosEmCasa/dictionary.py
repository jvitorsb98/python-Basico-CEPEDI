carro = {
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": 2016,
    "Cor": "Prata",
}

carro["Estado"] = "Batido"
carro.pop("Cor")

for x in carro:
    print(carro[x])

for c, v in carro.items():
    print(c + " " + str(v))

carro.clear()

if "Modelo" in carro:
    print("SIM")
else:
    print("Não")

print("Tamanho : " + str(len(carro)))

Carro1 = {
    "Fabricante": "Honda",
    "Modelo": "HRV"
}

Carro2 = {
    "Fabricante": "Volkswagen",
    "Modelo": "Golf"
}

Carro3 = {
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

carros = {
    "C1": Carro1,
    "C2": Carro2,
    "C3": Carro3,
}

for c in carros:
    for v in carros[c]:
        print(c +":"+ v +":"+ carros[c][v])
