t_carros = ("HRV","Golf","Argo")
l_carros = list(t_carros)
lt_carros = tuple(l_carros)


l_carros[2] = "Focus"


print(l_carros)
print(lt_carros)


for x in l_carros:
    print(x)