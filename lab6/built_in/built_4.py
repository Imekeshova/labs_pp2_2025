import math
import time

def delayed_sqrt(num1, delay_ms):
    time.sleep(delay_ms / 1000)  
    result = math.sqrt(num1)
    print(f"Square root of {num1} after {delay_ms} milliseconds is {result}")

num1 = int(input())  
delay_ms = int(input())  

delayed_sqrt(num1, delay_ms)
