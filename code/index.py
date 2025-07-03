print('Bem-vindos a Pizzaria de Beatriz Avelar')

print('Pizzas Salgadas (PS) / Pizzas Doces (PD) \nP - R$30,00  /  R$34,00 \nM - R$45,00  /  R$48,00\nG - R$60,00  /  R$66,00')

preco = 0
qtd = 0



while True:

  sabor = input('Qual sabor deseja? PS ou PD: ')

  if(sabor == 'PS'):
    tamanho = input('Qual tamanho deseja? P, M ou G: ')
    if(tamanho == 'P'):
      preco += 30.00
      qtd += 1
    elif(tamanho == 'M'):
      preco += 45.00
      qtd += 1
    elif(tamanho == 'G'):
      preco += 60.00
      qtd += 1
    else:
      print('Tamanho inexistente, tente novamente.')
      continue
    pedir = input('Deseja pedir mais alguma coisa? S ou N: ')
    if(pedir == 'S'):
      continue
    break

  if(sabor == 'PD'):
    tamanho = input('Qual tamanho deseja? P, M ou G: ')
    if(tamanho == 'P'):
      preco += 34.00
      qtd += 1
    elif(tamanho == 'M'):
      preco += 48.00
      qtd += 1
    elif(tamanho == 'G'):
      preco += 66.00
      qtd += 1
    else: 
      print('Tamanho inexistente, tente novamente.')
      continue
    pedir = input('Deseja pedir mais alguma coisa? S ou N: ')
    if(pedir == 'S'):
      continue 
    break

  else:
    print('Sabor inexistente, tente novamente.')
    continue



total = preco
print(f'Você pediu {qtd} pizzas. O valor total do pedido é de {total}')
