import time
import RPi.GPIO as GPIO
 
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import random
import sys, os
import logging
import multiprocessing
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gaListening = 20              
gaResponding = 26
phoneRinging = 16


GPIO.setup(gaListening, GPIO.IN)
GPIO.setup(gaResponding, GPIO.IN)
GPIO.setup(phoneRinging, GPIO.IN, GPIO.PUD_UP)

# Configure the count of pixels:
PIXEL_COUNT = 32
SHUT_DOWN = 14400

turned_off = False
#global stop
#stop = False
#p = multiprocessing.Process()

#def terminate_process():
	#global p
	#if p.is_alive():
		#p.terminate()

RGB = ()
 
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)
 
# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle_successive(wait=0.001):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                    # tricky math! we use each pixel as a fraction of the full 96-color wheel
                    # (thats the i / strip.numPixels() part)
                    # Then add in j which makes the colors go around per pixel
                    # the % 96 is to make the wheel cycle around
                pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
            pixels.show()
            if wait > 0:
                time.sleep(wait)

def setColor(RGB):
        r = int(RGB[0])
	#print (r)
        str(r)
	#print (r)
        int(r)
	#print (r)
        g = int(RGB[1])
	#print (g)
        b = int(RGB[2])
	#print (b)
        for i in range(pixels.count()):
            ga_Listening()
            ga_Responding()
            phone_Ring(pixels)
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()    
                
            
                
def rainbow_cycle(wait=0.005):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for j in range(256): # one cycle of all 256 colors in the wheel
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
                pixels.show()
                if wait > 0.0:
                    time.sleep(wait)
                
def rainbow_cycle_party(wait=0.005):
        for j in range(256): # one cycle of all 256 colors in the wheel
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
            pixels.show()
            if wait > 0.0:
                time.sleep(wait)
 
def rainbow_colors(wait=0.05):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for j in range(256): # one cycle of all 256 colors in the wheel
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
                pixels.show()
                if wait > 0:
                    time.sleep(wait)
                
def rainbow_colors_party(wait=0.05):
    for j in range(256): # one cycle of all 256 colors in the wheel
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
            pixels.show()
            if wait > 0:
                time.sleep(wait)
                

def red_one_by_one(pixels, wait=0.005, color=(255, 0, 0)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(pixels.count()):
                for j in reversed(range(i, pixels.count())):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    # first set all pixels at the begin
                    for k in range(i):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    # set then the pixel at position j
                    pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    if wait > 0:
                        time.sleep(wait)
                    
def green_one_by_one(pixels, wait=0.005, color=(0, 255, 0)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(pixels.count()):
                for j in reversed(range(i, pixels.count())):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    # first set all pixels at the begin
                    for k in range(i):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    # set then the pixel at position j
                    pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    if wait > 0:
                        time.sleep(wait)
                        
def blue_one_by_one(pixels, wait=0.005, color=(0, 0, 255)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(pixels.count()):
                for j in reversed(range(i, pixels.count())):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    # first set all pixels at the begin
                    for k in range(i):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    # set then the pixel at position j
                    pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    if wait > 0:
                        time.sleep(wait)
                    
def one_by_one_party(pixels, wait=0.005, color=(0, 0, 255)):
        #pos = 0
        for i in range(pixels.count()):
            for j in reversed(range(i, pixels.count())):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.clear()
                # first set all pixels at the begin
                for k in range(i):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    #pixels.clear()
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                # set then the pixel at position j
                pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                pixels.show()
                if wait > 0:
                    time.sleep(wait)
                    
def red_single_orbit(pixels, orbit_times=2, wait=0.05, color=(255, 0, 0)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for k in range(orbit_times):
            
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    #for k in range(i):
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #pixels.clear()
                    pixels.show()
                    time.sleep(wait)
                    pixels.clear()
                
def green_single_orbit(pixels, orbit_times=2, wait=0.05, color=(0, 255, 0)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for k in range(orbit_times):
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    #for k in range(i):
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #pixels.clear()
                    pixels.show()
                    time.sleep(wait)
                    pixels.clear()
            
def blue_single_orbit(pixels, orbit_times=2, wait=0.05, color=(0, 0, 255)):
    start =  time.time()
    turned_off = False
    while True:
        #pos = 0
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for k in range(orbit_times):
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.clear()
                    #for k in range(i):
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #pixels.clear()
                    pixels.show()
                    time.sleep(wait)
                    pixels.clear()
                
def single_orbit_party(pixels, orbit_times=2, wait=0.05, color=(0, 0, 255)):
        #pos = 0
        for k in range(orbit_times):
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.clear()
                #for k in range(i):
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                pixels.show()
                #pixels.clear()
                pixels.show()
                time.sleep(wait)
                pixels.clear()
                
def single_orbit_reverse_party(pixels, orbit_times=2, wait=0.05, color=(255, 0, 0)):
    # pos = 0
    for k in range(orbit_times):
        for i in reversed(range(pixels.count())):
            ga_Listening()
            ga_Responding()
            phone_Ring(pixels)
            pixels.clear()
            #for k in range(i):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
            pixels.show()
            #pixels.clear()
            pixels.show()
            time.sleep(wait)
            pixels.clear()
                
def strobe(pixels, blink_times=1, wait=0.15, color=(255,255,255)):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(blink_times):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                # blink two times, then wait
                pixels.clear()
                for j in range(2):
                    for k in range(pixels.count()):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #time.sleep(0.08)
                    pixels.clear()
                    pixels.show()
                    #time.sleep(0.08)
                time.sleep(wait)
            
def red_strobe(pixels, blink_times=1, wait=0.15, color=(255,0,0)):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(blink_times):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                # blink two times, then wait
                pixels.clear()
                for j in range(2):
                    for k in range(pixels.count()):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #time.sleep(0.08)
                    pixels.clear()
                    pixels.show()
                    #time.sleep(0.08)
                time.sleep(wait)
            
def green_strobe(pixels, blink_times=1, wait=0.15, color=(0,255,0)):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(blink_times):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                # blink two times, then wait
                pixels.clear()
                for j in range(2):
                    for k in range(pixels.count()):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #time.sleep(0.08)
                    pixels.clear()
                    pixels.show()
                    #time.sleep(0.08)
                time.sleep(wait)
                
def blue_strobe(pixels, blink_times=1, wait=0.15, color=(0,0,255)):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(blink_times):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                # blink two times, then wait
                pixels.clear()
                for j in range(2):
                    for k in range(pixels.count()):
                        ga_Listening()
                        ga_Responding()
                        phone_Ring(pixels)
                        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                    pixels.show()
                    #time.sleep(0.08)
                    pixels.clear()
                    pixels.show()
                    #time.sleep(0.08)
                time.sleep(wait)
                
def strobe_party(pixels, blink_times=10, wait=0.15, color=(0,0,255)):
        for i in range(blink_times):
            ga_Listening()
            ga_Responding()
            phone_Ring(pixels)
            # blink two times, then wait
            pixels.clear()
            for j in range(2):
                for k in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                pixels.show()
                #time.sleep(0.08)
                pixels.clear()
                pixels.show()
                #time.sleep(0.08)
            time.sleep(wait)
            
def twinkle(pixels, wait=0.07, color=(255,255,255)):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
                k = random.randint(0,31)
                #ga_Listening()
                #ga_Responding()
                #phone_Ring(pixels)
                for i in range(pixels.count()):
                    ga_Listening()
                    ga_Responding()
                    phone_Ring(pixels)
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                            # set then the pixel at position j
                pixels.show()
                if wait > 0:
                    time.sleep(wait)
                pixels.clear()
            
def twinkle_party(pixels, wait=0.07, color=(255,255,255)):
        for j in range (pixels.count()*2):
            k = random.randint(0,31)
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                        # set then the pixel at position j
            pixels.show()
            if wait > 0:
                time.sleep(wait)
                pixels.clear()

def twinkle_party_xmas(pixels, wait=0.07):
        for j in range (pixels.count()*2):
            k = random.randint(0,31)
            c = random.randint(0,1)
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                if c == 0:
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                        # set then the pixel at position j
                else:
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color(0, 255, 0))
            pixels.show()
            if wait > 0:
                time.sleep(wait)
                pixels.clear()
        
def sequence_off(wait=0.001):
    turned_off = False
    while True:
        for i in range(pixels.count()):
            ga_Listening()
            ga_Responding()
            phone_Ring(pixels)
            pixels.set_pixel_rgb(i, 0, 0, 0)
            pixels.show()
 
def decreaseBrightness(step = -5):
	for dc in range(0, 101, step):
		pwm.ChangeDutyCycle(dc)
		print(dc)
		
		
def increaseBrightness(step = 5):
	for dc in range(0, 101, step):
		pwm.ChangeDutyCycle(dc)
		print(dc)
		time.sleep(0.05)

def brightness_decrease(pixels, wait=0.01, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(25, r - step))
            g = int(max(25, g - step))
            b = int(max(25, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()
        if wait > 0:
            time.sleep(wait)
            
def brightness_increase(pixels, wait=0.01, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(255, r + step))
            g = int(max(255, g + step))
            b = int(max(255, b + step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def sequence_off1(wait=0.1, color=(0,0,0)):
        for i in range(pixels.count()):
            pixels.set_pixel_rgb(i, 255, 0, 0)
            pixels.show()
        for i in range(pixels.count()):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
            pixels.show()
            if wait > 0.0:
                time.sleep(wait)

def google(wait = 0.001):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            for i in range(0,8):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 128, 0, 0))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(8,16):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 64, 128))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(16,24):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(64, 64, 0))
                pixels.show()
                #if wait > 0.0:
                    #time.sleep(wait)
            for i in range(24,32):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 128, 0))
                pixels.show()
            if wait > 0.0:
                time.sleep(wait)

def xmas_eight(wait = 0.001):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
            for i in range(0,8):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 255, 0, 0))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(8,16):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(16,24):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                #if wait > 0.0:
                    #time.sleep(wait)
            for i in range(24,32):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
            if wait > 0.0:
                time.sleep(wait)

def xmas_eight_party(wait = 4):
 
            for i in range(0,8):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 255, 0, 0))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(8,16):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                    #if wait > 0.0:
                        #time.sleep(wait)
            for i in range(16,24):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                #if wait > 0.0:
                    #time.sleep(wait)
            for i in range(24,32):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
            if wait > 0.0:
                time.sleep(wait)

def xmas_two(wait = 0.001):
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off() 
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                time.sleep(2)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                time.sleep(2)
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                time.sleep(2)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                time.sleep(2)
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                time.sleep(2)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                time.sleep(2)
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                time.sleep(2)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                pixels.show()
                time.sleep(2)
                
            if wait > 0.0:
                time.sleep(wait)

def xmas_two_party(wait = 6):
            for i in range(pixels.count()):
                ga_Listening()
                ga_Responding()
                phone_Ring(pixels)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()
                time.sleep(2)
                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
                else:
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
                pixels.show()               
            if wait > 0.0:
                time.sleep(wait)


def ga_Listening():
    if (GPIO.input(gaListening) == True) and (GPIO.input(gaResponding) == False):
        listening = True
        print ("listening")
        #start = time.time()
        #pulse = 1.5
        for i in range(17,24):
            pixels.set_pixel_rgb(i, 128, 0, 0) #Google R)
        for i in range(25,32):
                pixels.set_pixel_rgb(i,0, 64, 128) #Google B)
        for i in range(0,8):
                pixels.set_pixel_rgb(i, 64, 64, 0) #Google Y)
        for i in range(9,16):
                pixels.set_pixel_rgb(i, 0, 128, 0) #Google G)
        pixels.show()
        print ("listening2")
        if (GPIO.input(gaResponding) == False) and (GPIO.input(gaListening) == False) and (listening == True):
            listening = False
            for i in range(pixels.count()):
                pixels.set_pixel_rgb(i, 20, 20, 20)
                pixels.show()
            print ("listening is false")
            #twinkle_party(pixels, wait=0.07, color=(0,0,0))
            #for i in range(32):
                #pixels.set_pixel_rgb(i, 0, 0, 0)
            #brightness_decrease(pixels)
            #pixels.show()
                 
def ga_Responding():
    if (GPIO.input(gaResponding) == True) and (GPIO.input(gaListening) == False):
        responding = True
        print ("responding")
        #start = time.time()
        #pulse = 1.5
        for i in range(8,15):
            pixels.set_pixel_rgb(i, 128, 0, 0) #Google R)
        for i in range(16,23):
            pixels.set_pixel_rgb(i,0, 64, 128) #Google B)
        for i in range(24,31):
            pixels.set_pixel_rgb(i, 64, 64, 0) #Google Y)
        for i in range(0,7):
            pixels.set_pixel_rgb(i, 0, 128, 0) #Google G)
        pixels.show()
        print ("responding2")
        #if (time.time() - pulse > 0):
            #brightness_decrease(pixels)
        #else:
           # start = time.time()
            #brightness_increase(pixels)
        if (GPIO.input(gaResponding) == False) and (GPIO.input(gaListening) == False) and (responding == True):
            responding = False
            for i in range(pixels.count()):
                pixels.set_pixel_rgb(i, 0, 0, 0)
                pixels.show()
            #twinkle_party(pixels, wait=0.07, color=(0,0,0))
            #print ("responding is false")
           
def default_color():
         for i in range(pixels.count()):
                pixels.set_pixel_rgb(i, 0, 0, 255)
                pixels.show()
            
           
        

def phone_Ring(pixels, blink_times=5, wait=0.1, color=(255,0,0)):
    if (GPIO.input(phoneRinging) == False):
        for i in range(blink_times):
            # blink two times, then wait
            pixels.clear()
            for j in range(2):
                for k in range(pixels.count()):
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
                pixels.show()
                #time.sleep(0.08)
                pixels.clear()
                pixels.show()
                #time.sleep(0.08)
            time.sleep(wait)
        
            
def party_xmas():
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            twinkle_party_xma(pixels, wait=0.07)s
            xmas_two_party(wait = 6)
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            xmas_eight_party(wait = 4)
            twinkle_party(pixels, wait=0.07, color=(0,255,0))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(0,255,0))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(255,0,0))
            twinkle_party_xmas(pixels, wait=0.07)
            strobe_party(pixels, blink_times=5, wait=0.15, color=(0,255,0))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(255,0,0))
            single_orbit_party(pixels, orbit_times=2, wait=0.05, color=(255, 0, 0))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 0))
            xmas_two_party(wait = 6)
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            twinkle_party(pixels, wait=0.07, color=(0,255,0))
            xmas_eight_party(wait = 4)
            twinkle_party_xma(pixels, wait=0.07)s
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(0, 255, 0))
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(0, 255, 0))
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            rainbow_colors_party(wait=0.05)
            twinkle_party_xmas(pixels, wait=0.07)
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(0, 255, 0))
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 0))
            rainbow_cycle_party(wait=0.005)
            strobe_party(pixels, blink_times=10, wait=0.15, color=(0,255,0))
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 0))
            xmas_two_party(wait = 6)
            strobe_party(pixels, blink_times=10, wait=0.15, color=(255,0,0))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 0))
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            twinkle_party(pixels, wait=0.07, color=(0,255,0))
            rainbow_cycle_party(wait=0.005)
            twinkle_party_xmas(pixels, wait=0.07)
            strobe_party(pixels, blink_times=5, wait=0.2, color=(255,0,0))
            strobe_party(pixels, blink_times=10, wait=0.1, color=(0,255,0))
            twinkle_party_xmas(pixels, wait=0.07)
            strobe_party(pixels, blink_times=15, wait=0.05, color=(255,0,0))
            strobe_party(pixels, blink_times=20, wait=0.02, color=(0,255,0))
            xmas_two_party(wait = 6)
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            twinkle_party(pixels, wait=0.07, color=(0,255,0))
            twinkle_party_xmas(pixels, wait=0.07)
        

def party():
    start =  time.time()
    turned_off = False
    while True:
        if not turned_off and time.time() > (start + SHUT_DOWN):
            sequence_off1()
            turned_off = True
            sequence_off()
        else:
            
            twinkle_party(pixels, wait=0.07, color=(255,0,255))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(0,255,0))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(255,0,0))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(0,0,255))
            strobe_party(pixels, blink_times=5, wait=0.15, color=(255,255,255))
            single_orbit_party(pixels, orbit_times=2, wait=0.05, color=(255, 0, 255))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 255))
            rainbow_colors_party(wait=0.05)
            twinkle_party(pixels, wait=0.07, color=(255,0,255))
            twinkle_party(pixels, wait=0.07, color=(0,0,255))
            rainbow_cycle_party(wait=0.005)
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 255))
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 255))
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(0, 0, 255))
            rainbow_colors_party(wait=0.05)
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(0, 0, 255))
            single_orbit_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            single_orbit_reverse_party(pixels, orbit_times=1, wait=0.05, color=(255, 0, 0))
            one_by_one_party(pixels, wait=0.005, color=(0, 255, 0))
            rainbow_cycle_party(wait=0.005)
            strobe_party(pixels, blink_times=10, wait=0.15, color=(255,255,255))
            twinkle_party(pixels, wait=0.07, color=(0,255,255))
            one_by_one_party(pixels, wait=0.005, color=(0, 0, 255))
            rainbow_colors_party(wait=0.05)
            strobe_party(pixels, blink_times=10, wait=0.15, color=(255,0,255))
            one_by_one_party(pixels, wait=0.005, color=(255, 255, 0))
            twinkle_party(pixels, wait=0.07, color=(255,0,0))
            rainbow_cycle_party(wait=0.005)
            strobe_party(pixels, blink_times=5, wait=0.2, color=(255,0,255))
            strobe_party(pixels, blink_times=10, wait=0.1, color=(0,255,255))
            strobe_party(pixels, blink_times=15, wait=0.05, color=(0,0,255))
            strobe_party(pixels, blink_times=20, wait=0.02, color=(255,255,255))
            rainbow_colors_party(wait=0.05)
            twinkle_party(pixels, wait=0.07, color=(255,0,255))
               
    

def clear_pixels():
	pixels.clear()
	pixels.show()
	


	

    
	
	
