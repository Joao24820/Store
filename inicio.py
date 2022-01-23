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
