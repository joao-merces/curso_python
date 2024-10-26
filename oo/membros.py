class Contador:
    contador = 0

    @classmethod
    def incremento(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def decremento(cls):
        cls.contador -= 1
        return cls.contador
    
c1 = Contador()

print(c1.incremento())
print(c1.incremento())
print(c1.incremento())
print(c1.incremento())
print(c1.incremento())
print(c1.incremento())
print(c1.decremento())
print(c1.decremento())
print(c1.decremento())
print(c1.decremento())
print(c1.decremento())

