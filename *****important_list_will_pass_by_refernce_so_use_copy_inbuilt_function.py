##########all topologial order problem 

### here we are passing multiple listes as arguments but they will be not pass by value it is pass by reference be take care abou this take c
@@@@@@@@@@copy in built import copy   and deepcopy() mehtod *********************** thank you
lot
!!!!!!!!!!!!!!!!!!!!!!


from collections import defaultdict
import copy
def print_orders(g1,ind11,order11,node,visited11 ,v1):
	#update ind
	visited1=copy.deepcopy(visited11)
	ind1=copy.deepcopy(ind11)
	order1=copy.deepcopy(order11)
	visited1[node]=True
	order1.append(node)

	for k in g1[node]:
		ind1[k]=ind1[k]-1

	for m in range(v1):
		if(ind1[m]==0 and visited1[m]==False):
			node=m

			print_orders(g1,ind1,order1,node,visited1,v1)

	if(len(order1)==6):	
		print(order1)
	return 

		




class Graph:
	def __init__(self,v):
		self.v=v
		self.g=defaultdict(list)
		self.ind=[0]*v
	def addEdge(self,u,v):
		self.g[u].append(v)
		self.ind[v]=self.ind[v]+1
	def print_all(self):

		visited=[False]*self.v
		visited2=copy.deepcopy(visited)
		for i in range(self.v):


			if(self.ind[i]==0 and visited[i]==False):
				order=[]
				node=i

				

				

				print_orders(self.g,self.ind,order,node,visited2,self.v)







graph = Graph(6)
graph.addEdge(5, 2) 
graph.addEdge(5, 0) 
graph.addEdge(4, 0) 
graph.addEdge(4, 1) 
graph.addEdge(2, 3) 
graph.addEdge(3, 1)
graph.print_all() 
  












output:
4 5 0 2 3 1 
4 5 2 0 3 1 
4 5 2 3 0 1 
4 5 2 3 1 0 
5 2 3 4 0 1 
5 2 3 4 1 0 
5 2 4 0 3 1 
5 2 4 3 0 1 
5 2 4 3 1 0 
5 4 0 2 3 1 
5 4 2 0 3 1 
5 4 2 3 0 1 
5 4 2 3 1 0 













