from multiprocessing import Queue
#imoprt Queue
q1=Queue()
for i in range(5):
  q1.put(i)
for j in range(5):
  print(q.get())
""" 
q1.empty()
q1.full()

"""

"""
import Queue

q = Queue.LifoQueue() #stack (indirectly)

#add items at the head of the queue
for x in range(4):
    q.put("item-" + str(x))
#remove items from the head of the queue
while not q.empty():
    print q.get()

#the output
item-3
item-2
item-1
item-0


"""
