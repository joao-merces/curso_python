# Dicionarios funcionam com chave valor e nao a indexação padrão 

alunos = {
    'nome': 'Pedro',
    'nota': 9.5,
    'ativo': True
}

print(type(alunos))
print(f"Nome: {alunos['nome']}");
print(f"Nota: {alunos['nota']}")