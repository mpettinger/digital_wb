import RPi.GPIO as GPIO
import numpy as np

class scale:
    def __init__(self,clk,data,name=None):
        assert isinstance(clk,int), f"Clock pin must be an integer"
        assert isinstance(data,int), f"Data pin must be an integer"
        self.clk = clk
        self.data = data
        self.intercept = 0
        self.slope = 0
        self.tare = 0
        if name == None:
            self.name = f"Scale on pin {self.data}"
        if name != None:
            self.name = name
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
        samples = []
        for i in range(n):
            samples.append(self.get_raw_reading())
        samples_np = np.array(samples)
        return (samples_np.mean(),samples_np.std())
    
   
   
   
    
    def get_weight(self):
        reading = self.get_avg_raw()
        weight = self.slope*reading[0] + self.intercept
        return weight - self.tare
            
    def clean_up(self):
        GPIO.cleanup([self.clk,self.data])