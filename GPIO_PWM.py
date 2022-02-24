import RPi.GPIO as GPIO #import de la librairie de controle des pins
from time import * #import de la librairie de controle du temps
 
ledPin = 12 #pin de la led (en GPIO.BOARD)
frequence = 100  #fréquence de la pin, 100 donc toutes les 0.01 secondes 
dC = 0 #Cycle d'activié a 0 donc éteint
 
GPIO.setmode (GPIO.BOARD) #On choisit le mode d'identification des pins
GPIO.setup(ledPin, GPIO. OUT) #On définit la pin GPIO.18 comme une sortie
 
 
pwm = GPIO.PWM(ledPin, frequence) #On met la pin GPIO.18 en mode PWM
pwm.start(dc) #On commence le cycle avec 0% d'activité
 
print("Pin de la led: %d\nFréquence: %i" %(ledPin, frequence)) #On donne les infos a l'utilisateur
 
try: 
    while True: #début de la boucle générale
        for dC in range(0, 100,5): #Cette boucle augmente le cycle d'activité et donc l'intensité de led
            pwm.ChangeDutyCycle (dc) #update le cycle d'activité
            print("Cycle d'activité: %s "%dC, end="\r") #On donne les infos a l'utilisateur
            sleep(0.05) #On attend pour ne pas surcharger le Raspberry
            
        for dc in range (100, 0, -5): #Cette boucle diminue le d'activité et donc l'intensité de led
            pwm.ChangeDutyCycle (dc)
            print("cycle d'activité: %s "%dC, end="\r")
            sleep(0.05)
 
except KeyboardInterrupt: #Code éxécuté si on interromp avec <ctrl + c>
    pwm.stop()
    GPIO.cleanup()

