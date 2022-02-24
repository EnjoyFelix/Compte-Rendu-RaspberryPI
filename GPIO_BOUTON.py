import RPi.GPIO as GPIO #import de la librairie de controle des pins
from time import * #import de la librairie de controle du temps
 
ledPin = 12 #pin de la led (GPIO.18)
butPin = 15 #pin du bouton (GPIO.22)
 
of = True #Variable de l'état de la led
 
GPIO.setmode(GPIO.BOARD) #On choisit le mode d'identification des pins
GPIO.setwarnings(False) #On désactive les avertissements

GPIO.setup(ledPin, GPIO.OUT)  #On définit la pin de la led comme une sortie
 
GPIO.setup(butPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) #On définit la pin du bouton commme une entrée (quand le bouton remonte)
GPIO.add_event_listener(butPin, GPIO.RISING) #On ajoute une évenment sur la pin du bouton (quand il remonte)
 
GPIO.output(ledPin, of) #On allume la pin de la led
 
print("Pin de la led: %d\nPin du bouton; %i" %(ledPin, butPin)) #on affiche les pins active a l'utilisateur
 
try:
    while True: #boucle générale
        if GPIO.event_detected(butPin): #Condition sur l'évenement défnit plus haut
            if of == True: #On inverse l'état de la led
                of = False
            else:
                of = True
            GPIO.output(ledPin, of) #...et on l'applique
            print("Etat du bouton: %s"%of, end="\r") #On affiche l'état de la led a l'utilisateur
            
except KeyboardInterrupt: #Code éxécuté si on interrompt la boucle avec <ctrl + c>
    GPIO.output(ledPin, GPIO.LOW) #On éteint la led
    print("")
    GPIO.cleanup() #On passe un ptit coup de ballet

