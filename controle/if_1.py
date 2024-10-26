nota = float(input("Informe a nota: "))
comportado = True if input('Comportado y/n: ') == 'y' else False

if nota >= 9 and comportado == True:
    print('Parabéns! :P')
    print('Quadro de Honra!')

elif nota >= 6 and nota < 9:
    print('Aprovado!')

elif nota >= 4 and nota < 6:
    print('Recuperação')

else:
    print('Reprovado')