def soma(a, b):
    return a + b

f = soma    # Guardou a função na variavel f

print(f(3,4))


def operacao_aritmetica(fn, a, b):
    return fn(a,b)

# Passando função como parametro
restultado = operacao_aritmetica(soma,13,48)    # passa a função soma como parametro para a função operacao_aritmetica, entao a funcao de operaçao invoca a função soma q retorna a soma para operacao que nos retorna o resultado final

print(restultado)

#Função retornar função

def soma_parcial(a):
    def concluir_soma(b):
        return a+b
    return concluir_soma

restultado_final = soma_parcial(10)(12)
print(restultado_final)

'''
primeiro passamos 10 para a função soma_parcial
a primeira executa o bloco de codigo dela, que tambem precisa
de um numero, logo passamos 12 para a soma_parcial que passa o 12
para a concluir soma, que retorna a+b para a função soma_parcial
e a soma_parcial retorna a função concluir_soma que tem a resposta
'''