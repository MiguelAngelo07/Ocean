print("Hello World")

nome = input("Qual o seu nome?")
print(f'Olá, {nome}, seja bem-vindo')

idade = int(input('Qual a sua idade?'))
if idade < 13:
    print('Criança')
elif idade < 18:
    print ('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')
