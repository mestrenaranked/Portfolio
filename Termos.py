from random import choice
advinhe = ["alugar","farpas","jornal","falhos","julgar","deuses","dormir","dexter","jarros","angulo","macaco","montar","muitos"] #[p.upper() for p in[ ]]
letras = choice(advinhe)
# print(letras)
chances = 5
print("Bem vindo ao Termos! É só digitar uma sequência de 6 letras: ")
while chances > 0:
  palavra = input("").lower() ###
  if palavra == letras:
      print(f"="*45,"\nAcertou🎉🎉🎉! \nParabéns, sinta se a vontade para jogar de novo.")
      break
  elif len(palavra) != 6:
      print("Tem q ter 6 letras👻👻👻!")
      continue
  acertos = []
  for i in range(6):
    if palavra[i] == letras[i]:
      acertos.append("✅")
    elif palavra[i] in letras:
      acertos.append("🟨")
    else:
      acertos.append("🟥")
  chances -= 1
  acertos.append(" ")
  acertos.append(f"{chances}/5")
  print("="*30)
  for l in palavra.capitalize(): print(f" ",l, end="")
  print(f" "*4,"Chances","\n", end="")
  print(f" ".join(acertos)) ###
if chances == 0:
  print("="*35,f"\nPerdeu😭😭😭! \nA palavra era {letras.capitalize()}, tente de novo.")
