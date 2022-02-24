import Adafruit_DHT #Import de la librairie du capteur DHT 22
from time import sleep #import du 'sleep' dans la librairie de controle du temps
 
capteur = Adafruit_DHT.DHT22 #On définit notre capteur comme un DHT 22
DHT_DATAPIN = 4 #GPIO 4
 
print("Hello World !") #On affiche un signe de vie
print("/!\ L'OPÉRATION PEUT PRENDRE JUSQUA 30 SECONDES !")
 
try: #Pour l'interruption de la boucle
    while True: #Boucle générale
        hum, temp = Adafruit_DHT.read_retry(capteur, DHT_DataPin) #On associe hum (humidité) et temp (température) a leurs valeur réspéctives)
        if hum!= None and temp != None: #Si le capteur marche
            print("Température:%f\tHumidité%f"%(temp,hum)) #On affiche les infos a l'utilisateur
        else: #Si le capteur marche pas
            print("ERREUR >")
        sleep(2) #On attend deux secondes avant de recommencer
   
except keyboardInterrupt:#Code éxécuté si on interrompt avec <ctrl + c>
    print("---------------")
    input("")
