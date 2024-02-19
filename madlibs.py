# Concatenação de strings
# vamos supor que precisamos criar uma string que diga: 'hoje é dia de ir ao _____'
# local = 'médico' # ou alguma outra variável

# métodos que podem ser usados:

# print('hoje é dia de ir ao ' + local)
# print('hoje é dia de ir ao {}'.format(local))
# print(f'hoje é dia de ir ao {local}')

# Completar a frase a seguir: Hoje é dia de ___, Quando acordei o dia estava ___ e um nevoeiro levemente frio tomava conta do lugar, dias assim existem somente para nos ___.

# Definindo variáveis
sub = input(
  'Inserir um substantivo coerente: ')

adj = input(
  'Inserir um adjetivo coerente: ')

vrb = input(
  'Inserir um verbo coerente: ')

# Montagem do texto
madlib = f"Hoje é dia de {sub}. \n Quando acordei, o dia estava {adj} e um nevoeiro levemente frio tomava conta do lugar, dias assim existem somente para nos {vrb}."

# Imprimindo na tela
print('\n', madlib)
