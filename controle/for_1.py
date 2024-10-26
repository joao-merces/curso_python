

for i in range(10):
    print(i)

# funciona como um for em C, porem não se declara o i, e o mesmo sempre comça do 0, e soma 1 a cada rodada, no limite especificado do range

print('sd')

for i in range(5,10):
    print(i)

#Funciona igual o de cima, porem começa do 5


print('sd')

for i in range(1,10,2):
    print(i)

#Funciona igual os de cima, porem começa do 1 e pula de 2 em 2 

num = [2,4,6,8,10,11]
print('da')
for n in num:
    print(n)

# Passa pela lista num


txt = 'Python é muito massa'

for i in txt:
    print(i, end=' ')
# end muda espaçamento, no caso de uma quebra de linha por um espaço

produto = {
    'nome': 'caneta',
    'preco': 0.5,
}
print('\n')
print('\n')
print('\n')

for atr in produto:
    print(atr, '->' ,produto[atr])