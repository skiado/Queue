
# Εϊσοδος στην ουρά
def enqueue(q, item):
	q.append(item)
	
# Έξοδος από την ουρά	
def dequeue(q):
        if len(q) < 1:
            return None
        return q.pop(0)

def display(q):
        print(q)
        
        
        
q1 = []
for i in range(10):
	enqueue(q1,i)
print(q1)	
while(len(q1) > 0):
	print(dequeue(q1),'->',q1)
	
