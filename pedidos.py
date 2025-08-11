print('Lanchonete da Mandy')
print('item 1 - Coxinha R$ 5,00')
print('item 2 - Pastel R$ 7,00')
print('item 3 - Café R$ 4,00')
print('item 4 - Suco R$ 6,00')
print('item 5 - Sair')

total = 0
while True:
  op = int(input('Qual item gostaria de comprar?'))
  

  if (op == 1):
    qtd = int(input('Quantas unidades comprar?'))
    total = total + qtd * 5.00
  
  elif (op == 2):
    qtd = int(input('Quantas unidades comprar?'))
    total = total + qtd * 7.00

  
  elif (op == 3):
    qtd = int(input('Quantas unidades comprar?'))
    total = total + qtd * 4.00


  elif(op == 4):
    qtd = int(input('Quantas unidades comprar?'))
    total = total + qtd * 6.00
  
  elif(op == 5):
    break
     
  else:
    print('Produto inválido. Selecione uma opção!')

print(f'O total a ser gasto é de: R${total}')
    



