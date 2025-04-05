from scale import scale
import time
s1 = scale(3,5)
while True:
    print(s1.get_avg_raw(n=100))
    time.sleep(.500)
s1.clean_up()
