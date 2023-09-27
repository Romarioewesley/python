peso = float(input ("digite o peso")) 
altura = float(input("digite a altura"))
imc = (altura **2) / peso
if imc <18.5:
  print("desnutrido")
if imc <25:
  print("normal")
if imc <30:
  print ("acima do Peso")
else:
  print("obeso")