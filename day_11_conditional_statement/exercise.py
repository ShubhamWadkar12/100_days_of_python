""" Create a python program capable of greeting you with Good Morning, 
Good Afternoon and Good Evening. Your program should use time module 
to get the current hour. Here is a sample program and documentation link for you
 """
 
import time
t =int(time.strftime('%I'))
if t < 12:
    print("Good morning")
elif t == 12:
    print("Good afternoon")
else:
    print("Good eveving")
