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
        element_to_index = {}

        queue = []
        level = []

        queue.append(vertex)
        index_to_element[counter] = vertex.data
        element_to_index[vertex.data] = counter
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
            # print("For the element {} -> adj list {} ".format(vertex.data, adjacency_list))
            queue.pop(0)

            if len(queue) == 0:
                # print("This is the element to index array ", element_to_index)
                # print("This is the index to element array ", index_to_element)
                return adjacency_list, index_to_element, element_to_index

            vertex = queue[0]  # Visit the next vertex need to be processed
            index_to_element[counter] = vertex.data
            element_to_index[vertex.data] = counter
            counter += 1

        # return adjacency_list


    # def transpose_graph(self, adjacency_list, index_to_element, element_to_index):
    #     '''With the given adjacency list reverse the pointers resulting in a full transposal'''
    #     for element_pointing_index, neighbors in enumerate(adjacency_list):
    #         # With this index we should be able to get the data that corresponds to the index

    #         # Example 0 should point to 1
    #         pointing_element = index_to_element[element_pointing_index] # This part is good
            
    #     #     print(neighbors)

    #         for index, neighbor in enumerate(neighbors):
    #             # First remove the neighbor
    #             print("")
    #             popped_neighbor = neighbors.pop(index)
    #             # print("Popped neighbor ", popped_neighbor)

    #             # Then add the pointing element to the popped neighbor's list of neigbors
    #             neighbor_index = element_to_index[popped_neighbor]


    #             adjacency_list[neighbor_index].append(pointing_element)
    #             print("For element {} there neighbors are {}".format(popped_neighbor, adjacency_list[neighbor_index]))

    #     return adjacency_list


    def transpose_graph(self, adjacency_list, index_to_element, element_to_index, incrementing_counter=None, vertex=None):

        # TODO What is being auto updated?
        if incrementing_counter is None and vertex is None:
            incrementing_counter = 0
            vertex = self.vertex


        # TODO What is the base case  # If all the vertices in a list of neighbors have been visited
        



        # What is the functionality to perform dfs



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

adjacency_list, index_to_element, element_to_index = graph.createdAdjacencyList()
print(adjacency_list)
print(index_to_element)

print(graph.transpose_graph(adjacency_list, index_to_element, element_to_index))

# Now that we have the adjacency list now what
