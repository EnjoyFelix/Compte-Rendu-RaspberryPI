import RPi.GPIO as GPIO #import de la librairie de controle des pins
 
ledPin = 12 #pin de la led (en GPIO.BOARD)
frequence = 0.5 #fréquence de la pin, .5 hz donc 2 secondes
dC = 50 #cycle d'activité (50 donc 50% donc la led sera allumé une seconde a chaque fois)
 
GPIO.setmode(GPIO.BOARD)  #On choisit le mode d'identification des pins
GPIO.setwarnings(False) #On désactive les avertissements
GPIO.setup(ledPin, GPIO.OUT) #On définit la pin GPIO.18 comme une sortie
 
pwm = GPIO.PWM(ledPin, frequence) #On met la pin GPIO.18 en mode PWM
pwm.start(dC) #On commence le cycle avec 50% d'activité
input("'Entrée' pour arrêter >") #Attend une input utilisateur pour finir
pwm.stop() #Arrete le cycle
