# TUPLA - semelhante a uma lista só que imutavel, NÃO consegue inserir, excluir, ordenar, alterar - mantem a integridade
# criar uma tupla de países - tupla inicia com parenteses e lista com colchetes
paises = ('Brasil', 'Paraguai', 'Romenia', 'França', 'Espanha', 'Portugal', 'Argentina', 'China', 'Japão', 'Tailandia', 'Italia')


#exibir a tupla
for pais in paises:
    print(pais)

print('\n')

#exibi o tipo de coleção
print(type(paises))

# após exeutado - não será mais possivel inserir e nem modificar os dados dessa tupla
paises_lista = sorted(paises) # esse é o unico comando que exibi uma tupla em forma de lista ordenada - ordem alfabetica

for pais in paises_lista:
    print(pais)

#  exemplo <class 'tuple'>
# Argentina
# Brasil
# China
# Espanha
# França
# Italia
# Japão
# Paraguai
# Portugal
# Romenia
# Tailandia
# PS C:\Users\Aluno Manhã\TURMA PYTHON IA VESP\tupla>