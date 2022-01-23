import  math

print('======== LOJAS SKY ========')
nome=str(input('Seja bem vindo, qual o nome do cliente: '))
tel=int(input('sr {} informe o seu numero de telefone com o DDD:'.format(nome)))
ender=str(input('Sr {} informe o seu endereço atual:'.format(nome)))
pro=str(input('sr {} informe o produto escolhido: '.format(nome)))
p=float(input('sr {} Informe o preço total gasto com o(a) {} R$'.format(nome,pro)))
print('FORMAS DE PAGAMENTO ')
print('[1] á vista dinheiro ou cheque\n[2] á vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
op=int(input('Qual a opção acima escolhida: '))

one=p*(10/100)
one1=p-one
one2=p*(5/100)
one22=p-one2
one4=p*(20/100)
one44=p+one4

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
