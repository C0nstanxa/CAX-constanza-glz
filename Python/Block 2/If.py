while True:
  a=int(input("adivina la contraseña:"))
  if(a==8):
    print("ADIVINASTE!!")
  if(a<8):
    print("te falta")
  if(a>8):
    print("te sobra")
  