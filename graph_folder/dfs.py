from collections import defaultdict



class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	def add_Edge(self,source,dest):
		self.graph[source].append(dest)
		self.graph[dest].append(source)
	def print_graph(self):
		len1=len(self.graph)
		for i in range(len1):
			list1=self.graph[i]
			list1.sort()
			print(i,end="")
			k=0
			len_list1=len(list1)
			while(k!=len_list1):
				print("->",end="")
				print(list1[k],end="")
				k=k+1
			print()
	def breadth_first_search(self):
		visited=defaultdict(lambda:0)
		stack=[]
		stack.append(2)

		while(stack):
			vi_point=stack.pop()
			if(visited[vi_point]==0):
				print(vi_point,end=" ")
			visited[vi_point]=1

			list3=self.graph[vi_point]

			list3.sort(reverse=True)
			for m in list3:
				if(visited[m]==0):
					stack.append(m)
		



			
g = Graph()
g.add_Edge(0, 1) 
g.add_Edge(0, 2) 
g.add_Edge(1, 2) 
g.add_Edge(2, 0) 
g.add_Edge(2, 3) 
g.add_Edge(3, 3) 
g.print_graph() 
g.breadth_first_search()


