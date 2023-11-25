curso = " Curso de Python"

a = curso.split(" ")
print(a)
print(curso.strip())
print(curso.replace("Python","C#"))

print(curso.strip().lower())

print("Tamanho : " + str(len(curso)))

res = "Python" in curso
print(res)

cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano=2019
canal = "CFB cursos"

data = "{}, {} de {} de {}\n\"{}\""

print(cidade + ", " + str(dia) + " de " + str(mes) + " de " + str(ano))
print(data.format(cidade,dia,mes,ano,canal))

