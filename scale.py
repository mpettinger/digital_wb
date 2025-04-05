import RPi.GPIO as GPIO
import time
import numpy as np

class scale:
    def __init__(self,clk,data):
        self.clk = clk
        self.data = data
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(clk,GPIO.OUT)
        GPIO.setup(data,GPIO.IN)
        GPIO.output(clk,GPIO.LOW)
        
        
    def get_raw_reading(self):
        GPIO.output(self.clk,GPIO.LOW)
        state = GPIO.input(self.data)
        while state == 1:
            state = GPIO.input(self.data)
        my_data = 0
        cycle = 27
        for i in range(cycle):
            GPIO.output(self.clk,GPIO.HIGH)
            GPIO.output(self.clk,GPIO.LOW)
            my_data = my_data + GPIO.input(self.data)*(2**(cycle-i))
        return my_data
    
    def get_avg_raw(self,n=10):
        samples = np.array()
        while samples.std() > 500:
        for i in range(n):
            samples.append(self.get_raw_reading())
        samples = np.array(samples)
        return (samples.mean(),samples.std())
    
    def calibrate(self):
        input("Make sure scale is empty and press enter.")
        low_weight = 0
        high_weight = float(input("Load scale and enter known weight in Kgs: "))
        slope = (low_weight - high_weight)/
    
    def clean_up(self):
        GPIO.cleanup([self.clk,self.data])