import RPi.GPIO as GPIO
import time

led_r=21
led_g=4
led_b=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_r, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_b, GPIO.OUT)

def red(detik):
    print("merah nyala!")
    GPIO.output(led_r, GPIO.HIGH)
    GPIO.output(led_g, GPIO.LOW)
    GPIO.output(led_b, GPIO.LOW)
    time.sleep(detik)

def green(detik):
    print("hijau nyala!")
    GPIO.output(led_r, GPIO.LOW)
    GPIO.output(led_g, GPIO.HIGH)
    GPIO.output(led_b, GPIO.LOW)
    time.sleep(detik)

def blue(detik):
    print("biru nyala!")
    GPIO.output(led_r, GPIO.LOW)
    GPIO.output(led_g, GPIO.LOW)
    GPIO.output(led_b, GPIO.HIGH)    
    time.sleep(detik)

def exit():
    GPIO.cleanup() #mematikan semua pin yang sudah dipake diprogram

def main():
    red(5)
    green(5)
    blue(5)
    exit()

if __name__ == '__main__':
        main()
