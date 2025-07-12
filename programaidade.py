"""Faça um programa que leia nome, idade e sexo de 4 pessoas. No final
o programa deve mostrar a média de idade das pessoas
O nome do homem mais velho
Quantas mulheres tem menos de 20 anos."""
velhohomem = 0
velhonome = ''
mulherjovem = 0
idadetotal = 0
for a in range(1, 5):
    #ENTRADA
    print(f'======= {a}° PESSOA =======')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    #ESTRUTURA
    idadetotal += idade
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido, Digite M/F: '))
    if sexo == 'F' and idade <20:
        mulherjovem += 1
    if sexo == 'M' and idade > velhohomem:
        velhohomem = idade
        velhonome = nome
mediaidade = idadetotal / 4

#SAÍDA
print(f'A idade média das pessoas é {mediaidade:.1f}.')
print(f'O homem mais velho é {velhonome}, e sua idade é {velhohomem}.')
if mulherjovem == 0:
    print('Não tem mulheres com menos de 20 anos.')
else:
    print(f'Há {mulherjovem} mulheres com menos de 20 anos.')