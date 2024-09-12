import networkx as nx
import matplotlib.pyplot as plt

def main():

    numVillages = 0 
    numLines = 0
    start = "" 
    end = ""


    startEstablished = False
    endEstablished = False

    counter = 0

    G = nx.DiGraph()

    vertex_dict = {}

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

                id = (startVillage, endVillage, company, type)
                reverse_id = (endVillage, startVillage, company, type)

                if len(G.nodes) == 0:
                    G.add_node(id)
                    G.add_node(reverse_id)
                else:
                    G.add_node(id)
                    G.add_node(reverse_id)


                    if len(vertex_dict) > 0:
                        if endVillage in vertex_dict:
                            neighbors = vertex_dict[endVillage]
                            for neighbor in neighbors:

                                neighborStart = neighbor[0]
                                neighborEnd = neighbor[1]
                                neighborCompany = neighbor[2]
                                neighborType = neighbor[3]

                                if company == neighborCompany and type == neighborType: 
                                    G.add_edge(id, neighbor, weight = 10)
                                    print("added edge between " + id[0] + id[1] + " and " + neighbor[0] + neighbor[1] + " weight 10")
                                elif company == neighborCompany and type != neighborType:
                                    G.add_edge(id, neighbor, weight = 12)
                                    print("added edge between " + id[0] + id[1] + " and " + neighbor[0] + neighbor[1] + " weight 12")
                                elif company != neighborCompany and type == neighborType:
                                    G.add_edge(id, neighbor, weight = 15)
                                    print("added edge between " + id[0] + id[1] + " and " + neighbor[0] + neighbor[1] + " weight 15")
                        if startVillage in vertex_dict:
                            neighbors = vertex_dict[startVillage]
                            for neighbor in neighbors:
                                
                                neighborStart = neighbor[0]
                                neighborEnd = neighbor[1]
                                neighborCompany = neighbor[2]
                                neighborType = neighbor[3]

                                
                                if company == neighborCompany and type == neighborType: 
                                    G.add_edge(reverse_id, neighbor, weight = 10)
                                    print("added reverse edge between " + reverse_id[0] + reverse_id[1] + " and " + neighbor[0] + neighbor[1] + " weight 10")
                                elif company == neighborCompany and type != neighborType:
                                    G.add_edge(reverse_id, neighbor, weight = 12)
                                    print("added reverse edge between " + reverse_id[0] + reverse_id[1] + " and " + neighbor[0] + neighbor[1] + " weight 12")
                                elif company != neighborCompany and type == neighborType:
                                    G.add_edge(reverse_id, neighbor, weight = 15)
                                    print("added reverse edge between " + reverse_id[0] + reverse_id[1] + " and " + neighbor[0] + neighbor[1] + " weight 15")

                if startVillage not in vertex_dict:
                    vertex_dict[startVillage] = [id]
                else:
                    vertex_dict[startVillage].append(id)
                if endVillage not in vertex_dict:
                    vertex_dict[endVillage] = [reverse_id]
                else:
                    vertex_dict[endVillage].append(reverse_id)



            counter += 1

    potentialStarts = vertex_dict[start]
    potentialEnds = []
    finalNode = vertex_dict[end]

    for key in vertex_dict:
        for node in vertex_dict[key]:
            if node[1] == end:
                potentialEnds.append(node)

    G.add_node("pseudoStart")
    G.add_node("pseudoEnd")


    for node in potentialStarts:
       G.add_edge("pseudoStart", node)
    for node in potentialEnds:
        G.add_edge(node, "pseudoEnd")

    path, path_length = nx.single_source_dijkstra(G, source="pseudoStart", target="pseudoEnd")
    print(path)
    print(path_length)

    printdict(vertex_dict)

    nx.draw(G, with_labels=True)
    plt.show()

def printdict(dict):
    for cluster in dict:
        print(cluster + " ", end="")
        for node in dict[cluster]:
            print(node[0] + node[1] + " ", end="")
        print()


if __name__ == "__main__":
    main()

                                                    
