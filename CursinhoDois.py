from builtins import input, print

valor_um = input('digite o primeiro valor ai pai ')
valor_dois = input('digite o segundo valor agora ')
if valor_um > valor_dois:
    print('o primeiro valor e maior')
elif valor_um < valor_dois:
    print('O segundo valor e maior')
elif valor_um == valor_dois:
    print ('os valores sao iguais')
else:
    print('que merda que e esse valor')
