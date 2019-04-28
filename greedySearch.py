import numpy as np

class Node(object):

	def __init__(self, elementos = np.array([]), node_father = None):
		self.elementos = elementos
		self.node_father = node_father
		self.heristica = self.heuristica()

	def heuristica(self):
		return None

	def print_state(self):

		array_path = np.array([])
		helper = self

		array.path.np.hstack(0, helper)

		helper = helper.father


		print(array_path)



node = Node()
print(node)