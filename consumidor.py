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
	
class Producer(Thread):
    """
	Appends integers to a queue.
	"""
    def __init__(self, t, q, a, b, p):
        """
        Thread t to add integers in [a,b] to q, sleeping between 1 and p seconds.
        """
        Thread.__init__(self, name=t)
        self.queue = q
        self.begin = a
        self.end = b
        self.pace = p 
        
    def run(self):
        """
		produces integers at some pace.
		"""
        print (self.getName() + " starts...")
        for i in range(self.begin, self.end+1):
            rnd = randint(1, self.pace)
            print (self.getName() + \
				"sleeps %d seconds" % rnd)
            sleep(rnd)
            print ("appending %d to queue" % i)
            self.queue.append(i)
        print ("Productor terminado")
		
def main():
	"""
	creates a producer object.
	"""
	que = []
	prd = Producer('producer', que, 3, 9, 10)
	prd.start()
	prd.join()
if __name__=="__main__":
	main()


#Añadir un hola mundo
print("Hola Mundo");
	
	
	
			
