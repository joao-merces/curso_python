from functools import reduce

alunos = [
    {'nome':'ana','nota':7.2},
    {'nome':'kauan','nota':5},
    {'nome':'deivid','nota':7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 5

obter_nota = lambda aluno:aluno['nota']

alunos_aprovados = filter(aluno_aprovado, alunos)

print(obter_nota(alunos[2] ))
print(alunos_aprovados)