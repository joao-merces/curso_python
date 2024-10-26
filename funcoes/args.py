#PEP -> python enrichment propose

def soma(*nums):        # *nums se refere a esperar uma tupla
    total = 0

    for i in nums:
        total += i
    
    return total

def resultado_final(**kwargs):  # **kwargs se refere a esperar um dicionario
    
    situacao = 'aprovado' if kwargs['nota']>=6 else 'reprovado'
    return situacao