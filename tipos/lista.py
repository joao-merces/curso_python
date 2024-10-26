nums = [1,2,3]    # Cria uma lista com os numeros 1,2 e 3

nums.append(4)      # add algo no apendice da lista nums

print(len(nums))        # Mostra o tamanho da lista nums
print(type(nums))

nums[3] = 100       # Muda o terceiro elemento da lista para 100 (começa do 0)
print(nums)

nums.insert(0, -200)    # Insere o -200 na posição 0, e passa o resto para uma casa posterior

print(nums[4])  # acessa o elemento de indice 4 da lista