import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
#Assign a pin
clk = 3#orange
data = 5 #yellow

GPIO.setup(clk,GPIO.OUT)
GPIO.setup(data,GPIO.IN)

GPIO.output(clk,GPIO.LOW)
my_data = GPIO.input(data)
while my_data == 1:
    my_data = GPIO.input(data)

print(f"data is ready{type(my_data)}")


for i in range(24):
    GPIO.output(clk,GPIO.HIGH)
    GPIO.output(clk,GPIO.LOW)
    my_data = my_data + GPIO.input(data)*(2**(24-i))


print(f"DATA: {my_data}")
GPIO.output(clk,GPIO.LOW)
#Cleanup
GPIO.cleanup([clk,data])