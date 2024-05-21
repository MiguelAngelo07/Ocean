#print("Hello World")

# nome = input("Qual o seu nome? ")
# print(f'Olá, {nome}, seja bem-vindo')

# idade = int(input('Qual a sua idade? '))
# if idade < 13:
    # print('Criança')
#elif idade < 18:
    # print ('Adolescente')
# elif idade < 60:
    # print('Adulto')
# else:
    # print('Idoso')


num = int(input('Entre com um número: '))
if num < 0:
    print(f'{num}, Valor lido é negativo')
else:
    print(f'{num}, Valor é positivo.')

num = int(input('Entre com um número: '))
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')

if (num % 2 == 0) and (num % 3 == 0):
    print (f'{num} é divisível por 2 e 3')
else:
    print(f'{num} não é divisível por 2 e 3')
    
