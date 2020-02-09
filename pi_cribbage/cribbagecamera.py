import time
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
from RPLCD import CharLCD
from RPi import GPIO

button = Button(17)
camera = PiCamera()
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13,6,5,11], numbering_mode = GPIO.BCM)

def capture():
    lcd.clear()
    lcd.cursor_pos = (0,1)
    lcd.write_string('taking picture')
    time.sleep(1)
    lcd.clear()
    print("Taking a picture")
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/automatedcribbage/pi_cribbage/images/%s.jpg' % timestamp)
    lcd.cursor_pos = (0,1)
    lcd.write_string('picture taken')
    lcd.cursor_pos = (1,3)
    lcd.write_string('waiting...')

button.when_pressed = capture
lcd.cursor_pos = (0,2)
lcd.write_string('waiting for')
lcd.cursor_pos = (1,4)
lcd.write_string('input...')

pause()
