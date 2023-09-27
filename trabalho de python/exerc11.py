preço = float(input("digite o preço"))
ex_pag = (input("escolha a forma de pagamento"))
if ex_pag ==1:
    valor_pago =preço- (preço*0.10)
elif ex_pag ==2:
    valor_pago =preço- (preço*0.15)
elif ex_pag ==3:
    valor_pago =preço
elif ex_pag ==4:
    valor_pago =preço+ (preço*0.10)
else:
  print("o valor inserido esta incorreto")