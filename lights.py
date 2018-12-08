from flask import Flask, flash, redirect, render_template, request, session, abort
import sys, os
sys.path.append(os.getcwd() + '/audio-reactive-led-strip/python/')#append entire directory
import logging
import multiprocessing
import light_control, visualization
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIXEL_COUNT = 32
SHUT_DOWN = 14400

turned_off = False

SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(32, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)



app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
global stop
stop = False
#global rainbow_cycle
p = multiprocessing.Process()
run = False
#r = 0
#g = 0
#b = 0



def terminate_process():
        global p
        if p.is_alive():
                p.terminate()
def loop_rainbow_cycle_successive(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.rainbow_cycle_successive()
                
def loop_party(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.party()

def loop_party_xmas(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.party_xmas()
                
def loop_sequence_off(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.sequence_off()
                
def loop_google(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.google()

def loop_xmas_two(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.xmas_two()

def loop_xmas_eight(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control.xmas_eight()
                
def loop_off(name):
        global stop
        while 1:
                if stop == True:
                        break
                light_control_off()             

def loop_rainbow_cycle(name, effect):
        global stop
        global rainbow_cycle
        while 1:
                if stop == True:
                        break
                if effect == "rainbow_cycle_very_fast":
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.005)
                elif effect == "rainbow_cycle_fast":
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.05)
                elif effect == "rainbow_cycle_medium":
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.3)
                elif effect == "rainbow_cycle_slow":
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.6)
                elif effect == "rainbow_cycle_very_slow":
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.9)
                else:
                        rainbow_cycle.rainbow_cycle_effect = light_control.rainbow_cycle(wait=0.4)
                        

def loop_rainbow_colors(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "rainbow_colors_very_fast":
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.005)
                elif effect == "rainbow_colors_fast":
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.05)
                elif effect == "rainbow_colors_medium":
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.3)
                elif effect == "rainbow_colors_slow":
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.6)
                elif effect == "rainbow_colors_very_slow":
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.9)
                else:
                        rainbow_colors.rainbow_colors_effect = light_control.rainbow_colors(wait=0.4)
                        
def loop_red_one_by_one(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "red_one_by_one_very_fast":
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=0.005)
                elif effect == "red_one_by_one_fast":
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=0.05)
                elif effect == "red_one_by_one_medium":
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=0.5)
                elif effect == "red_one_by_one_slow":
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=1.0)
                elif effect == "red_one_by_one_very_slow":
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=3.0)
                else:
                        red_one_by_one.red_one_by_one_effect = light_control.red_one_by_one(pixels, wait=0.5)
                        
def loop_green_one_by_one(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "green_one_by_one_very_fast":
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=0.005)
                elif effect == "green_one_by_one_fast":
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=0.05)
                elif effect == "green_one_by_one_medium":
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=0.5)
                elif effect == "green_one_by_one_slow":
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=1.0)
                elif effect == "green_one_by_one_very_slow":
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=3.0)
                else:
                        green_one_by_one.green_one_by_one_effect = light_control.green_one_by_one(pixels, wait=0.5)
                        

                        
def loop_blue_one_by_one(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "blue_one_by_one_very_fast":
                        blue_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=0.005)
                elif effect == "blue_one_by_one_fast":
                        blue_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=0.05)
                elif effect == "blue_one_by_one_medium":
                        blie_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=0.5)
                elif effect == "blue_one_by_one_slow":
                        blue_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=1.0)
                elif effect == "blue_one_by_one_very_slow":
                        blue_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=3.0)
                else:
                        blue_one_by_one.blue_one_by_one_effect = light_control.blue_one_by_one(pixels, wait=0.5)
                        
def loop_red_single_orbit(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "red_single_orbit_very_fast":
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=0.005)
                elif effect == "red_single_orbit_fast":
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=0.05)
                elif effect == "red_single_orbit_medium":
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=0.5)
                elif effect == "red_single_orbit_slow":
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=1.0)
                elif effect == "red_single_orbit_very_slow":
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=3.0)
                else:
                        red_single_orbit.red_single_orbit_effect = light_control.red_single_orbit(pixels, wait=0.5)
                        
def loop_green_single_orbit(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "green_single_orbit_very_fast":
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=0.005)
                elif effect == "green_single_orbit_fast":
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=0.05)
                elif effect == "green_single_orbit_medium":
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=0.5)
                elif effect == "green_single_orbit_slow":
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=1.0)
                elif effect == "green_single_orbit_very_slow":
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=3.0)
                else:
                        green_single_orbit.green_single_orbit_effect = light_control.green_single_orbit(pixels, wait=0.5)
                
def loop_blue_single_orbit(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "blue_single_orbit_very_fast":
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=0.005)
                elif effect == "blue_single_orbit_fast":
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=0.05)
                elif effect == "blue_single_orbit_medium":
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=0.5)
                elif effect == "blue_single_orbit_slow":
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=1.0)
                elif effect == "blue_single_orbit_very_slow":
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=3.0)
                else:
                        blue_single_orbit.blue_single_orbit_effect = light_control.blue_single_orbit(pixels, wait=0.5)

def loop_strobe(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "white_strobe":
                        strobe.strobe_effect = light_control.strobe(pixels, color=(255,255,255))
                elif effect == "red_strobe":
                        strobe.strobe_effect = light_control.strobe(pixels, color=(255,0,0))
                elif effect == "green_strobe":
                        strobe.strobe_effect = light_control.strobe(pixels, color=(0,255,0))
                elif effect == "blue_strobe":
                        strobe.strobe_effect = light_control.strobe(pixels, color=(0,0,255))
                else:
                        strobe.strobe_effect = light_control.strobe(pixels, color=(255,255,255))
                        
def loop_twinkle(name, effect):
        global stop
        while 1:
                if stop == True:
                        break
                if effect == "white_twinkle":
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(255,255,255))
                elif effect == "pink_twinkle":
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(255,0,255))
                elif effect == "red_twinkle":
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(255,0,0))
                elif effect == "green_twinkle":
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(0,255,0))
                elif effect == "blue_twinkle":
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(0,0,255))
                else:
                        twinkle.twinkle_effect = light_control.twinkle(pixels, color=(255,255,255))
                    


RGB = (u'0', u'0', u'0')                
def loop_setColor(name):
        global stop
        start = time.time()
        turned_off = False
        while 1:
            if not turned_off and time.time() > (start + SHUT_DOWN):
                light_control.sequence_off1()
                turned_off = True
                light_control.sequence_off()
            else:
                if stop == True:
                        break
                light_control.setColor(RGB)

                
def loop_visualization(name, effect):
        if effect == "visualize_energy":
                visualization.visualization_effect = visualization.visualize_energy
        elif effect == "visualize_scroll":
                visualization.visualization_effect = visualization.visualize_scroll
        elif effect == "visualize_spectrum":
                visualization.visualization_effect = visualization.visualize_spectrum
        else:
                visualization.visualization_effect = visualization.visualize_spectrum

        # Initialize LEDs
        visualization.led.update()
        # Start listening to live audio stream
        visualization.microphone.start_stream(visualization.microphone_update)

@app.route("/")
def index():
     return render_template(
        'index.html')
        
@app.route("/getColor/", methods=['POST'])

def getColor():
        global stop
        global p
        stop = False
        global RGB
        terminate_process()
        RGB = (request.form['r'],request.form['g'],request.form['b'])
        print (RGB)
        light_control.setColor(RGB)
        p = multiprocessing.Process(target=loop_setColor, args=("loop_setColor", ))
        p.start()
        return render_template('index.html')
    
@app.route("/useFunction/", methods=['POST'])
def useFunction():
        global stop
        global p
        stop = False
        func = request.form['function']
        if func == "rainbow_cycle_successive":
                terminate_process()
                p = multiprocessing.Process(target=loop_rainbow_cycle_successive, args=("loop_rainbow_cycle_successive",))
                p.start()
        elif func == "sequence_off":
                terminate_process()
                light_control.sequence_off1() # note that sequence_off1 runs once, sequence off is looped
                p = multiprocessing.Process(target=loop_sequence_off, args=("loop_sequence_off",))
                p.start()
                
        elif func == "rainbow_cycle":
                terminate_process()
                effect = request.form['rainbow_cycle_effect']
                p = multiprocessing.Process(target=loop_rainbow_cycle, args=("loop_rainbow_cycle", effect))
                p.start()
                
        elif func == "rainbow_colors":
                terminate_process()
                effect = request.form['rainbow_colors_effect']
                p = multiprocessing.Process(target=loop_rainbow_colors, args=("loop_rainbow_colors", effect))
                p.start()
                
        elif func == "red_one_by_one":
                terminate_process()
                effect = request.form['red_one_by_one_effect']
                p = multiprocessing.Process(target=loop_red_one_by_one, args=("loop_red_one_by_one", effect))
                p.start()
                
        elif func == "green_one_by_one":
                terminate_process()
                effect = request.form['green_one_by_one_effect']
                p = multiprocessing.Process(target=loop_green_one_by_one, args=("loop_green_one_by_one", effect))
                p.start()
                
        elif func == "blue_one_by_one":
                terminate_process()
                effect = request.form['blue_one_by_one_effect']
                p = multiprocessing.Process(target=loop_blue_one_by_one, args=("loop_blue_one_by_one", effect))
                p.start()
                
        elif func == "red_single_orbit":
                terminate_process()
                effect = request.form['red_single_orbit_effect']
                p = multiprocessing.Process(target=loop_red_single_orbit, args=("loop_red_single_orbit", effect))
                p.start()
                
        elif func == "green_single_orbit":
                terminate_process()
                effect = request.form['green_single_orbit_effect']
                p = multiprocessing.Process(target=loop_green_single_orbit, args=("loop_green_single_orbit", effect))
                p.start()
                
        elif func == "blue_single_orbit":
                terminate_process()
                effect = request.form['blue_single_orbit_effect']
                p = multiprocessing.Process(target=loop_blue_single_orbit, args=("loop_blue_single_orbit", effect))
                p.start()
                
        elif func == "strobe":
                terminate_process()
                effect = request.form['strobe_effect']
                p = multiprocessing.Process(target=loop_strobe, args=("loop_strobe", effect))
                p.start()
                
        elif func == "twinkle":
                terminate_process()
                effect = request.form['twinkle_effect']
                p = multiprocessing.Process(target=loop_twinkle, args=("loop_twinkle", effect))
                p.start()
                
        #elif func == "sequence_off":
            #terminate_process()
            #p = multiprocessing.Process(target=loop_sequence_off, args=("loop_sequence_off",))
            #p.start()
            #light_control.sequence_off()
            #p = multiprocessing.Process(target=loop_off, args=("loop_off",))
            #p.start()
            #light_control.off()
            #terminate_process()
            
        elif func == "party":
                terminate_process()
                p = multiprocessing.Process(target=loop_party, args=("loop_party",))
                p.start()
        elif func == "party_xmas":
                terminate_process()
                p = multiprocessing.Process(target=loop_party, args=("loop_party_xmas",))
                p.start()
        elif func == "xmas_two":
                terminate_process()
                p = multiprocessing.Process(target=loop_party, args=("loop_xmas_two",))
                p.start()
        elif func == "xmas_eight":
                terminate_process()
                p = multiprocessing.Process(target=loop_party, args=("loop_xmas_eight",))
                p.start()  
        elif func == "google":
                terminate_process()
                p = multiprocessing.Process(target=loop_google, args=("loop_google",))
                p.start()
        elif func == "visualization":
                terminate_process()
                effect = request.form['visualization_effect']
                p = multiprocessing.Process(target=loop_visualization, args=("loop_visualization", effect ))
                p.start()
        elif func == "inc_brightness":
                light_control.increaseBrightness()
        elif func == "dec_brightness":
                light_control.decreaseBrightness()
        elif func == "STOP":
                stop = True
                terminate_process()
                light_control.clear_pixels()
                
        #elif func == "sequence_off":
            #terminate_process()
            #p = multiprocessing.Process(target=loop_sequence_off, args=("loop_sequence_off",))
            #p.start()
        
        
                

        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
    
    
                
                
    
    
