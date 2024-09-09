import networkx as nx
import matplotlib.pyplot as plt

def main():

    numVillages = 0 
    numLines = 0
    start = "" 
    end = ""

    counter = 0

    G = nx.Graph()

    vertex_dict = {}
    keyring = set()

    with open("maze.txt") as file:
        for line in file:
            initialData = line.split()
            if counter == 0:
                numVillages = int(initialData[0])
                numLines = int(initialData[1])
                start = initialData[2]
                end = initialData[3]
            else:
                startVillage = initialData[0]
                endVillage = initialData[1]
                company = initialData[2]
                type = initialData[3]

                id = "" + startVillage + endVillage

                if len(G.nodes) == 0:
                    G.add_node(id)
                else:
                    G.add_node(id)
                    if startVillage in keyring:
                        neighbors = vertex_dict[startVillage]
                        for neighbor in neighbors:
                            G.add_edge(id, neighbor)
                    
                if startVillage not in keyring:
                    vertex_dict[startVillage] = [id]
                    keyring.add(startVillage)
                else:
                    vertex_dict[startVillage].append(id)
                    keyring.add(startVillage)
            
            counter += 1


    nx.draw(G, with_labels=True)
    plt.show()

    shortest = nx.shortest_path(G, start, end)
    print("shortest path is " + shortest)

if __name__ == "__main__":
    main()

                                                    
