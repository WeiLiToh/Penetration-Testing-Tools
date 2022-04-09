#!/usr/bin/python3

import socket 

class Scanner:
	def __init__(self, ip):
		self.ip = ip
		self.open_ports = []

	def __repr__(self):
		return 'Scanner: {}'.format(self.ip)

	def is_open(self, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.2)		
		availability_status = s.connect_ex((self.ip, port))
		s.close()
		return availability_status

	def scan(self, lowerport, upperport):
		for port in range(lowerport, upperport + 1):
			if self.is_open(port) == 0:
				self.add_port(port)

	def add_port(self, port):
		self.open_ports.append(port)

	def write(self, filepath):
		pass 	

def main():
	ip = input("Please enter the ip address that you want to scan: ")
	scanner = Scanner(ip)
	lowerport, upperport = input("Please enter the range of ports you want to scan in the format <int>-<int>: ").split()
	scanner.scan(int(lowerport), int(upperport))
	print(scanner.open_ports)

if __name__ == "__main__":
	main()	

# 137.74.187.101 --> Hackthissite.org
