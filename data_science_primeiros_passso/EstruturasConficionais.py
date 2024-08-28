#if

media = 4
e_aluno = True
idade = 10

if (media > 5):
    print('passou')
else:
    print('nao pasou')

#elif

if (media == 5):
    print('aluno fazer nova prova')
elif (media > 5):
    print('passou')
else:
    print('nao passou')

#operadores logicos
if (media > 5 and e_aluno):
    print('passou')
elif (idade == 10 or e_aluno):
    print('nao passou')
elif(not e_aluno):
    print('nao e aluino')

lista = 'Carlos, Bezerra, Angelica, Freitas'
nome = 'Carlos'

if (nome in lista):
    print(nome)