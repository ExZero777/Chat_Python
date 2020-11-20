import socket
import threading
import sys
import pickle
import pybase64

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host="localhost", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input('->')
			if msg != 'salir':
				b = msg.encode("UTF-8")
				msg = pybase64.b64encode(b)
				self.send_msg(msg)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					data = pickle.loads(data)
					data = pybase64.b64decode(data)
					data = data.decode("UTF-8")
					print(data)
			except:
				pass

	def send_msg(self, msg):    
		self.sock.send(pickle.dumps(msg))


c = Cliente()
		