if op ==1:
    print('sr {} o valor de R${:.2f} terá 10% de desconto sendo cobrado R${:.2f}'.format(nome,p,one1))
if op ==2:
     print('sr {} o valor de R${:.2f} terá 10% de desconto sendo cobrado R${:.2f}'.format(nome,p,one22))
if op ==3:
     print('sr {} o valor de R${:.2f}, ficará por R${:.2f} durante 2 meses sem acrescimo'.format(nome,p,p/2))
if op ==4:
    print('sr {} o valor de R${:.2f} terá 20% de juros sendo cobrado R${:.2f}'.format(nome,p,one44))
    j=int(input('Informa quantas vezes gostaria de dividir o valor R${:.2f} : '.format(one44)))
    s=one44 / j
    print('Sr {} o valor de cada parcela ficará por R${:.2f} durante {} meses'.format(nome,s,j))
if op>=5:
    print('OPÇÃO INVALIDA !')
    print('Sr {} tente novamente !!'.format(nome))
