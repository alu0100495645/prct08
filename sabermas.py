#!/usr/bin/python
#|encoding:UTF-8

print "Introduzca el nombre del fichero donde se encuentran los resultados:"
nombre_fich= raw_input();

 # Una forma de averiguar si un fichero existe o no puede ser esta
 # debemos de incluir el paquete os.path
 # 	if os.path.isfile(nombre_fich):
 #		fichero=open(nombre_fich,"a")
 #	else:
 #		fichero=open(nombre_fich,"w")
 # Otra forma puede ser mediante excepciones, como vemos a continuacion:
 
try:
  fichero=open(nombre_fich)
  linea=fichero.readline()
  while(linea !=""):
    aprox=int(linea.split()[3])
    print("Nº de intervalos: %d" % (aprox))
    for i in range (5):
      linea= fichero.readline()
      porcentaje=linea.split()[0]
      umbral=float(linea.split()[6])
      print("%s de fallos para el umbral %2.5f" %(porcentaje,umbral))
    linea=fichero.readline()

except:
    print "El nombre del fichero introducido es incorrecto"
    