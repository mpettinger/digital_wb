from scale import scale
import time
s1 = scale(3.1,5)
s1.calibrate()
continue_ = "GO"
while continue_ != "Q":
    continue_ = input("Enter Q to stop: ")
    for i in range(5):
        print(s1.get_weight())
        time.sleep(.500)
s1.clean_up()
