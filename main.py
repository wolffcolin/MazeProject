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
    vertex_dictEnd = {}
    keyring = set()
    keyringEnd = set()

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

                id = line

                if len(G.nodes) == 0:
                    G.add_node(id)
                else:
                    G.add_node(id)
                    
                    if len(keyring) > 0 and len(vertex_dict) > 0:
                        if startVillage in keyring:
                            neighbors = vertex_dict[startVillage]
                            for neighbor in neighbors:

                                info = neighbor.split()
                                neighborStart = info[0]
                                neighborEnd = info[1]
                                neighborCompany = info[2]
                                neighborType = info[3]

                                if company == neighborCompany and type == neighborType: 
                                    G.add_edge(id, neighbor, weight = 10)
                                elif company == neighborCompany and type != neighborType:
                                    G.add_edge(id, neighbor, weight = 12)
                                elif company != neighborCompany and type == neighborType:
                                    G.add_edge(id, neighbor, weight = 15)

                    if len(keyringEnd) > 0 and len(vertex_dictEnd) > 0:
                        if endVillage in keyringEnd:
                            neighbors = vertex_dictEnd[endVillage]
                            for neighbor in neighbors:
                                
                                info = neighbor.split()
                                neighborStart = info[0]
                                neighborEnd = info[1]
                                neighborCompany = info[2]
                                neighborType = info[3]

                                if company == neighborCompany and type == neighborType: 
                                    G.add_edge(id, neighbor, weight = 10)
                                elif company == neighborCompany and type != neighborType:
                                    G.add_edge(id, neighbor, weight = 12)
                                elif company != neighborCompany and type == neighborType:
                                    G.add_edge(id, neighbor, weight = 15)
   
                    if startVillage not in keyring:
                        vertex_dict[startVillage] = [id]
                        keyring.add(startVillage)
                    else:
                        vertex_dict[startVillage].append(id)
                        keyring.add(startVillage)

                    if endVillage not in keyringEnd:
                        vertex_dictEnd[endVillage] = [id]
                        keyringEnd.add(endVillage)
                    else:
                        vertex_dictEnd[endVillage].append(id)
                        keyringEnd.add(endVillage)
            
            counter += 1


    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()

                                                    
