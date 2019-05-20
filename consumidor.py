from threading import Thread
from random import randint
from time import sleep

class Consumer(Thread):
	"""
	Pops integers from a queue.
	"""
	
	def __init__ (self, t, q, n, p):
		"""
		Thread t to pop n integers from q.
		"""
		Thread.__init__(self, name=t)
		self.queue = q
		self.amount = n
		self.pace = p
	
	def run(self):
		"""
		Pops integers at some pace.
		"""
		print ("Consumption starts...")
		for i in range(0, self.amount):
			rnd = randint(1, self.pace)
			print(self.getName() + " sleeps %d seconds" %rnd)
			sleep(rnd)
			
			while True:
				try:
					i = self.queue.pop(0)
					print ("Popped %d from queue" %i)
					break
				except IndexError:
					print ("Wait a second...")
					sleep(1)
		print("Consumption terminated")
		
	
	
def main():
	"""
	Simulates consumption on somo queue
	"""
	que = range(5)
	cns = Consumer('Consumer', que, 5, 10)
	cns.start()
	cns.join()
	
if __name__ == '__main__':
	main()
	
			
