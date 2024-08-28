#Listas

lista = ['carlos bezerra', 9.5, 9.0,8.8, True]
print(lista)
print(lista[-1])

for elemento in lista:
    print(elemento)

#manipulacao em lista
#len
print(len(lista))
#particao
print(lista[1:2])
#append()
lista.append(6.0)
print(lista)

#extend
lista.extend([4.0,8.0,5.0])
print(lista)

#remove
print(lista)

#Dicionario

dicionario = {
    'chave_1' : 1,
    'chave_2' : 2
}

print(dicionario)
print(dicionario['chave_2'])
#metodos
dicionario.pop('chave_1')

print(dicionario.items())
print(dicionario.keys())
print(dicionario.values())




