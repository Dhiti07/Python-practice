#greet the user
import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if timestamp<="12:00" :
   print("good morning respected user")
elif timestamp<="16:00" : 
    print("good afternoon respected user")
else :
    print("good evening respected user")