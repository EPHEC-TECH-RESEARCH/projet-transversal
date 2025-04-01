from gpiozero import AngularServo
from time import sleep

# le servo moteur du projet transversal n'accepte pas les paramètres standards. Utilisez :
servo = AngularServo(18, min_angle=-90, max_angle=90,min_pulse_width=0.5e-3,max_pulse_width=2.5e-3)

while True:
    print('-90')
    servo.angle = -90
    sleep(5)
    print('-45')
    servo.angle = -45
    sleep(5)
    print('0')
    servo.angle = 0
    sleep(5)
    print('45')
    servo.angle = 45
    sleep(5)
    print('90')
    servo.angle = 90
    sleep(5)
