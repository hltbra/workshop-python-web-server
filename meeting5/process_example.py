from __future__ import print_function
import os


print("[{}] before fork".format(os.getpid()))
outside_array = range(10**5)
pid = os.fork()
if pid == 0:  # inside child process
   child_array = range(10**5)
   print("[{}] in child. ppid = {}".format(os.getpid(), os.getppid()))
else:
   print("[{}] in parent. ppid = {}".format(os.getpid(), os.getppid()))

raw_input("[{}] waiting for enter\n".format(os.getpid()))

