import socket
import threading
import sys
import pickle
import pybase64
from tkinter import *

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host="localhost", port=4000):		
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		top = Tk()
		top.title("Chat_Python_Decode")

		def send():
			msg = f"Usted => {self.e.get()}"
			self.txt.insert(END,"\n"+msg)

			b = self.e.get().encode("UTF-8")
			msg = pybase64.b64encode(b)
			self.send_msg(msg)

			self.e.delete(0,END)

		top.bind('<Return>', send)

		self.txt = Text(top)
		self.txt.grid(row=0,column=0,columnspan=2)

		self.e = Entry(top,width=100)

		send = Button(top,text="Enviar",command=send).grid(row=1,column=1)

		self.e.grid(row=1,column=0)

		top.mainloop()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					data = pickle.loads(data)
					print(data)
					data = pybase64.b64decode(data)
					data = data.decode("UTF-8")
					msg = f"Extraño => {data}"
					self.txt.insert(END,"\n"+msg)
			except:
				pass

	def send_msg(self, msg):    
		self.sock.send(pickle.dumps(msg))


c = Cliente()
		