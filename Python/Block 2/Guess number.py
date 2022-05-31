
while True:
  adivina=int(input("ingresa un numero:"))
  if adivina < 10:
    print('te falta mucho')
  if adivina > 150:
    print ('te pasaste por mucho')
  if adivina >= 56:
    print ('te pasaste')
  if adivina <= 54:
    print('te falta ')
  if adivina ==55:
    print('LO LOGRASTE!')
    break