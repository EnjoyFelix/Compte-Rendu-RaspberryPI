import RPi.GPIO as GPIO #importe la librairie de contrôle des pins
from time import * #importe la librairie de contrôle du temps
 
HIGH = GPIO.HIGH #J'associe ces deux valeurs pour la compréhension
LOW = GPIO.LOW
 
ledPin = 12 #Pin sur laquelle est branché la led
 
GPIO.setmode(GPIO.BOARD) #Met le bon mode d’identification des pins
GPIO.setup(ledPin, GPIO.OUT) #définit la pin 11 comme une sortie
 
try: #Début d'une boucle permettant l'arrêt du code à tout moment
    while True:
        GPIO.OUTPUT(ledPin, HIGH) #On Allume la led
        print("HIGH", end= "\r") #On donne l'info à l'utilisateur
        sleep(1) #On attend une seconde
        GPIO.OUTPUT(ledPin, LOW) #On éteint la led
        print("LOW ", end= "\r") #On donne l'info à l'utilisateur
        sleep(1) #On attend une seconde
 
#...et on recommence tant que l'utilisateur ne veut pas l'arrêter
 
except KeyboardInterrupt: #Le programme exécute ça si la boucle est cassée par <ctrl + c>
    print("")
    GPIO.output(ledPin, LOW)
