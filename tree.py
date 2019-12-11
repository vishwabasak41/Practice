
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	def set_data(self,data):
		self.data=data
	def get_data(self):
		return self.data
	def get_left(self):
		return self.left
	def get_right(self):
		return self.right

class binarytree:

	def __init__(self):
		self.root=None
		self.size=0
	def get_size(self):
		return size

	def insert(self,root,data):
		#print(self)
		#print("--listing attributes--")
		#print(self.__dict__)
		if root==None:
			root=Node(data)
			print("Node created : ",root,"and attributes are : ",root.__dict__)
			print("Created root node with data : ",root.data, " Left is : ",root.left," right : ",root.right) 
		else:
			print("in else")
			print("else root data",root.data)
			if data<root.data:
				root.left=self.insert(root.left,data)
				print("root node with data : ",root.data, " Left is : ",root.left.data)
			else:
				root.right=self.insert(root.right,data)
				print("root node with data : ",root.data," right : ",root.right.data)
		print("current root : ",root.data)
		return root
	
	def printTree(self,root):
		if root==None:
			return
		else:
			print(root.data)
			#print("/     \\")	
			self.printTree(root.left)
			self.printTree(root.right)

	def getSize(self,root):
		if root==None:
			return 0
		else:
			self.size=self.size+1
			self.getSize(root.left)
			self.getSize(root.right)
			return self.size



l=input().split(' ')
l=[int(x) for x in l]
print("l :",l)

root=None
print("initital root : ",root)
bt=binarytree()


for i in range(0,len(l)):

	if i>0:
		print("value : ",l[i],"and root value",root.data)
	else:
		print("value : ",l[i])

	root=bt.insert(root,l[i])
print("last value of root : ",root.data)
bt.printTree(root)
print("attributes",bt.__dict__)
size=bt.getSize(root)
print("size is : ",size)
print("completed")





	


		