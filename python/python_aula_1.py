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


#num = int(input('Entre com um número: '))
# if num < 0:
#    print(f'{num}, Valor lido é negativo')
#else:
#    print(f'{num}, Valor é positivo.')

# num = int(input('Entre com um número: '))
#if num % 2 == 0:
#    print(f'{num} é par')
#else:
#   print(f'{num} é ímpar')

#if (num % 2 == 0) and (num % 3 == 0):
#    print (f'{num} é divisível por 2 e 3')
#else:
#    print(f'{num} não é divisível por 2 e 3')

#idade = int(input('Qual a sua idade? '))
#if idade < 1:
#    print('Idade inválida')
#elif idade <= 13:
#    print('Você é uma criança.')
#elif idade >=14 and idade < 17:
#    print('Você é um adolescente.') 
#elif idade >= 18 and idade < 60:
#    print('Você é maior de idade')
#else:
#    print('Você é um idoso')

#idade = int(input('Qual sua idade? '))
# if (idade >= 18) and (idade <= 60):
#    print('Idoso')
#else:
#      print('Menor de idade')
#    else:
#        print('Maior de idade')


#if idade <= 0:
#    print('Idade inválida por favor coloque entre 1 a 120 anos')
#if not (idade >= 18) and not (idade >= 60):
#    print('Menor de idade.')
#else:
#    if not (idade > 60):
#        print('Maior de idade.')
#    else:
#        print('Idoso')
#print('isso sempre será impresso.')

#if idade < 13:
#    print('Criança.')
##elif idade < 18:
 #   print('Adolescente')
#elif idade < 60:
#    print('Adulto')
#else:
#    print('Idoso')


nota_1 = float(input('Digite sua nota 1: '))
nota_2 = float(input('Digite sua nota 2: '))
nota_3 = float(input('Digite sua nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3 

if nota_1 or nota_2 or nota_3 < 0:
    print('Digite uma nota válida')

if media >= 8: 
    print('Parabéns Você está aprovado!!')
elif media >= 6 and media < 8:
    print('Realize a prova final. ')
else:
    print('Você está reprovado =( ')