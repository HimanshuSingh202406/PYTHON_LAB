class Graph:
    def _init_(self):
        self.graph = dict()

    # edges are represented as 
    # {Node_1: (Node_2, Weight_1), Node_2: (Node_3, Weight_2)}
    def add(self, node, child, weight):
        self.graph[node] = (child, weight)

    def display(self):
        print(self.graph)


ob = Graph()
ob.add(1, 2, 2)
ob.add(2, 3, 4)
ob.display()
