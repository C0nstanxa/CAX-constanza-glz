numero=8 

compara=int(input("numero?"))

if(compara<numero):
  print("te falta")

#elif necesita de un if para funcionar 
elif(compara>numero):
  print("te sobra")

#es todo lo contrario dek IF, no del elif
else:
  print("felicidades")