import requests
import os


class proxy:
	def __init__(self):
		self.path = "proxy.txt"
	def get_proxy(self):
		if os.path.exists(self.path) == False:
			exit("Error (file not found)!")
		self.file = open(self.path, "r")
		self.file_read = self.file.readlines()
		for i in range(len(self.file_read)):
			self.file_read[i] = self.file_read[i].split("\n")[0]
		return self.file_read


class url:
	def __init__(self):
		self.path = "catalog.txt"
	def get_url(self):
		if os.path.exists(self.path) == False:
			exit( "Error (file not found)!")
		self.file = open(self.path, "r")
		self.file_read = self.file.readlines()
		for i in range(len(self.file_read)):
			self.file_read[i] = self.file_read[i].split("\n")[0]
		return self.file_read

class phone:
	def __init__(self):
		self.path = "nomber.txt"
	def get_nomber(self):
		os.system("python generate.py 1200")
		self.file = open(self.path, "r")
		self.file_read = self.file.readlines()
		for i in range(len(self.file_read)):
			self.file_read[i] = self.file_read[i].split("\n")[0]
		return self.file_read





