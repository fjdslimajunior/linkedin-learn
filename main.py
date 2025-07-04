from time import gmtime, srtftime

semaforo = "amarelo"

if (semaforo == "verde") :
    print("Liberador!")
else: 
    print("Aguarde!")

srtftime("%a, %H, %i", gmtime())
