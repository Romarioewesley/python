nome = input("digitr seu nome")
sexo = input("digite M ou F para seu sexo")
estadocivil = input("digite solteira ou casada")
if sexo== "F" and estadocivil == "casada":
  tempocasada = int(input("digite seu tempo de casada em anos"))
  print (nome, "é uma mulher casada á" , tempocasada)
else:
  print(nome, "não é uma mulher casada ")