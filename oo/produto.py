class Produto:
    def __init__(self, nome, preco):    # Instancia o objeto (inicia o objeto), Como se fosse um construtor
        self.nome = nome
        self.preco = preco

    @property
    def preco_final(self):
        return (1 - 0.3) * self.preco

p1 = Produto('TV',1800)
p2 = Produto('Caderno',12)

print(f'Produto {p1.nome}, R$ {p1.preco}, e o preço final sera de R$ {p1.preco_final}')

print(f'Produto {p2.nome}, R$ {p2.preco}')


# Classe são como moldes
# as instanciações são as coisas em si