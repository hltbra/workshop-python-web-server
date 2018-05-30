from __future__ import print_function
import threading

message = 'unset'
array = []

def task(msg):
   global message
   array.extend(range(10 ** 5))
   message = msg

t1 = threading.Thread(target=task, args=('ola mundo',))
t1.start()

t2 = threading.Thread(target=task, args=('hello world',))
t2.start()

t1.join()
t2.join()

raw_input("message = '{}'\n".format(message))

