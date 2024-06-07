# importar o módulo
# import modulo

# -> importar apenas uma função do módulo
# from modulo import calcular_circulo

# -> importar mais de uma função do módulo
# from modulo import calcular_circulo, calcular_quadrilatero

#  entrada de dados usando "int" para números inteiros
# b = int(input('Informe o valor da base: '))
# h = int(input('Informe o valor da altura: '))

# exibe o resultado do quadrilátero
# print(f'Área do quadrilátero: {modulo.calcular_quadrilatero(b, h)}.')

# -> exibe o resultado do quadrilátero usando a importação de mais de uma função do módulo
# print(f'Área do quadrilátero: {calcular_quadrilatero(b, h)}.')

# -> entrada de dados usando "float" para números decimais
# r = float(input('Informe o valor do raio: '))

# exibe a área da circunferência
# print(f'Área do círculo: {modulo.calcular_circulo(r)}.')

# -> entrada de dados usando "str" e "replace" para números decimais usando também a vírgula na hora de inserir os dados
# r = str(input('Informe o valor do raio: ')).replace(',', '.')
# r = float(r)

# # exibe a área da circunferência
# print(f'Área do círculo: {modulo.calcular_circulo(r)}.')

# -> exibe a área da circunferência usando apenas a importação de uma única função
# print(f'Área do círculo: {calcular_circulo(r)}.')