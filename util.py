
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        # set the index of the vertices dict to a vertex id
        # make the value of that index a set to hold the values of the edges
        self.vertices[vertex_id] = set()

    def add_edge(self, fromV, toV):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        # check that both the from vertex and the to vertex both exist in the graph
        if fromV in self.vertices and toV in self.vertices:
            # add the edge
            self.vertices[fromV].add(toV)
        else:
            # if the vertices dont exist, raise error to add
            raise IndexError('vertex (vertices) do not exist in graph, add to graph first')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        # return the vertex listing
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # create empty queue using the Queue class provided
        queue = Queue()
        # created empty set to house the visited nodes
        visited = set()
        # plac the starting_vertex in the queue
        queue.enqueue(starting_vertex)
        # while the queue is not empty
        while queue.size() > 0:
            # take the vertex out of the queue
            vertex = queue.dequeue()
            # if the vertex has not already been visited
            if vertex not in visited:
                # add the vertex to the visited set
                visited.add(vertex)
                print(vertex)
                # loop through all the next vertices of the neighbors of the vertex
                for next_vertex in self.get_neighbors(vertex):
                    # add those neighbors to the queue and then loop
                    queue.enqueue(next_vertex)
        # return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # create an epty stack using the Stack class provided
        stack = Stack()
        # create empty set to house all of the visited nodes
        visited = set()
        # push the starting vertex into the stack
        stack.push(starting_vertex)
        # while the stack is not empty
        while stack.size() > 0:
            # pop the vertex out of the queue
            vertex = stack.pop()
            # if the vertex is not already in the visited set
            if vertex not in visited:
                # add the vertex to the visited stack
                visited.add(vertex)
                print(vertex)
                # check the next vertx using get neighbors 
                for next_vertex in self.get_neighbors(vertex):
                    # add those neighbors to the stack and then loop
                    stack.push(next_vertex)
        # return visited

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        # check if starting vertex is in self.visited
        if starting_vertex not in self.visited:
            # if its not, add it
            self.visited.add(starting_vertex)
            # print the starting vertex
            print(starting_vertex)
            # loop through the neighbors
            for next_v in self.get_neighbors(starting_vertex):
                # self.visited.add(next_v)
                # and then do it all over again
                self.dft_recursive(next_v)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # # pass  # TODO
        # create empty queue using the Queue class provided
        queue = [[starting_vertex]]
        # created empty set to house the visited nodes
        visited = []
        # if your starting vertex is your destination
        if starting_vertex == destination_vertex:
            # yay youre done, return the queue
            return queue
        # while there is a queue
        while queue:
            # path becomes the popped vertex
            path=queue.pop(0)
            # this vertex becomes the last element in the path array
            vertex = path[-1]
            # if that vertex has not been visited yet
            if vertex not in visited:
                # loop through its neighbors
                for next_v in self.get_neighbors(vertex):
                    # create a new path for each neighbor, starting with the initial path
                    new_path = list(path)
                    # add the neighbor to the new path
                    new_path.append(next_v)
                    # add the new path to the queue
                    queue.append(new_path)
                    # when you finally reach the destination vertex
                    if next_v == destination_vertex:
                        # yay you found it, return the new path
                        return new_path
                # add the vertex to the visited array
                visited.append(vertex)
        # if no desstination vertex ever found, exit
        return 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        # initial stack with the starting vertex
        stack = [[starting_vertex]]
        # create an empty array to house all the visited vertice
        visited = []
        # if your starting vertex is the destination vertex
        if starting_vertex == destination_vertex:
            # yay you found it, return your stack
            return stack
        # while you have a stack
        while stack:
            # path is the vertex popped of the stack
            path = stack.pop(0)
            # this vertex becomes the last vertex in the path
            vertex = path[-1]
            # if that vertex has not been visited
            if vertex not in visited:
                # get its neighbors and loop through
                for next_v in self.get_neighbors(vertex):
                    # then create a new path for each neighbor beginning with the path to get there
                    new_path = list(path)
                    # add each neighbor to the new path
                    new_path.append(next_v)
                    # insert the new path at the beginning of the stack
                    stack.insert(0, new_path)
                    # if the neighbor is the destination
                    if next_v == destination_vertex:
                        # return the new path
                        return new_path
                # if not, add the vertex to the visited array
                visited.append(vertex)
        # if the desitination is never reached, return
        return

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # pass  # TODO
        # if this is the first loop and visited is None
        if visited is None:
            # set visited to a set
            visited = set()
        # add th starting vertex to the visited set
        visited.add(starting_vertex)
        # path then becomes the existing path plus the starting vertex
        # print("path before adding vertex", path)
        # path.append(starting_vertex)
        path = path + [starting_vertex]
        # print("path after adding vertex", path)
        # if the starting vertex is the destination
        if starting_vertex == destination_vertex:
            # then return that path
            return path
        # if its not the destination, get the neighbors of that vertex
        for next_v in self.get_neighbors(starting_vertex):
            # if taht neighbor has not been visted
            if next_v not in visited:
                # new path becomes the recursive call, passing in the neighbor, the destination, th current visited et and the current path
                new_path = self.dfs_recursive(next_v, destination_vertex, visited, path)
                # if there is a new_path
                if new_path:
                    # return that path from start to finish
                    return new_path
        # if no path can be found, return
        return None

