from collections import defaultdict



class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	def add_edge(self,source,dest):
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
		queue=[]
		queue.append(0)

		while(queue):
			vi_point=queue.pop(0)
			if(visited[vi_point]==0):
				print(vi_point,end=" ")
			visited[vi_point]=1

			list3=self.graph[vi_point]

			list3.sort()
			for m in list3:
				if(visited[m]==0):
					queue.append(m)
		



			
graph = Graph() 
graph.add_edge(0, 1) 
graph.add_edge(0, 4) 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 
graph.print_graph() 
graph.breadth_first_search()


