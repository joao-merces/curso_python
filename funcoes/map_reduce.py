from functools import reduce

# Caso queiramos aumentar todos as notas em 1,5. Poderiamos:

#notas = [6.4,7.7,5.8,8.4]

# Usar for

# for i, nota in range(len(notas)):
#     notas[i] = notas[i] + 1.5;

# usando maping --> maping pega uma lista converte em outra igual so que com uma informação ja mapeada

def add_um_meio(nota):
    return nota + 1.5

notas = [6.4,7.7,5.8,8.4]

notas_finais = map(add_um_meio,notas)

print(notas_finais)


# Reduce -> primeira parametro acumulador e o se=gundo o elemento atual
def soma(a,b):
    return a+b

total = reduce(soma, notas, 0)
print(total)