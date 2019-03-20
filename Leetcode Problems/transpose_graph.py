class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False  # Vertex hasn't been visited when instantiated or initially


def add_edge(x_vertex, y_vertex):  
    '''Given two vertices in a directed graph add the y_vertex as a neighbor of the x_vertex'''

    x_vertex.neighbors.append(y_vertex)  # Why is y_vertex's neighbors being appended to?

    return x_vertex


class Graph(object):
    def __init__(self, vertex):
        self.vertex = vertex

    def createdAdjacencyList(self):
        '''Using the vertex passed through the initializers create the adjacency list'''

        print("STARTING VERTEX ", self.vertex.neighbors)
        vertex = self.vertex

        adjacency_list = []
        index_to_element, counter = {}, 0

        queue = []
        level = []

        queue.append(vertex)
        index_to_element[counter] = vertex.data
        counter += 1

        while len(queue) > 0:  # Meaning there are vertices left to process
            for neighbor in vertex.neighbors:
                level.append(neighbor.data)

                # Only add for processing if hasnt been visited already or not in the queeu
                if neighbor.visited is False and neighbor not in queue:
                    queue.append(neighbor)

            # Once you have appended a vertex's list of neighbors we then want to append the level
            adjacency_list.append(level)
            vertex.visited = True  # Set to true because you have added neighbor nodes
            level = []  # Clear level for the next vertice's neighbors

            # What vertex to go to next
            print("For the element {} -> adj list {} ".format(vertex.data, adjacency_list))
            queue.pop(0)

            if len(queue) == 0:
                return adjacency_list, index_to_element

            vertex = queue[0]  # Visit the next vertex need to be processed
            index_to_element[counter] = vertex.data
            counter += 1

        # return adjacency_list


    def transpose_graph(self, adjacency_list):
        '''With the given adjacency list reverse the pointers resulting in a full transposal'''
        pass



first_vertex = Vertex(1)  # First Vertex has a connection to 2 and 4
second_vertex = Vertex(2)
third_vertex = Vertex(3)
fourth_vertex = Vertex(4)
fifth_vertex = Vertex(5)


# Space complexity O(2E) where E represents the edges since we are using an undirected graph we consume twice the space when creating these edges 
add_edge(first_vertex, second_vertex)
# add_edge(first_vertex, fourth_vertex)

# add_edge(second_vertex, first_vertex)
add_edge(second_vertex, third_vertex)

add_edge(third_vertex, first_vertex)
add_edge(third_vertex, fourth_vertex)

add_edge(fourth_vertex, fifth_vertex)
add_edge(fifth_vertex, first_vertex)



graph = Graph(first_vertex)  # Hopefully first vertex contains reference to other vertices

print(graph.createdAdjacencyList())

# Now that we have the adjacency list now what
