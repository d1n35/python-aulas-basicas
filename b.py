materia1 = float(input("Insira nota na matéria 1"))
materia2 = float(input("Insira nota na matéria 2"))
materia3 = float(input("Insira nota na matéria 3"))
notafinal = ((materia1+materia2+materia3)/3)
if notafinal>6:
  print("Você foi aprovado com a nota final de ",notafinal)
if notafinal<6:
  print("Você foi reprovado com a nota final de ",notafinal)
