alt = float(input("digite sua altura"))
sexo = input("digite M ou F para seu sexo")
if sexo == "M":
  ps_ideal=(72.7 * alt)-58
  print("o peso ideal do homem com altura de", alt, "é" ,ps_ideal,"kg")
elif sexo == "F":
  ps_ideal=(62.1* alt)-44.7
  print("o peso ideal da mulher com altura de", alt, "é" ,ps_ideal,"kg")