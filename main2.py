import networkx as nx
import matplotlib.pyplot as plt

def main():

    numVillages = 0 
    numLines = 0
    start = "" 
    end = ""

    dictionaryInit = False

    G = nx.DiGraph()

    vertex_dict = {}

    counter = 0

    masterlist = []

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

                inNode = (startVillage, endVillage, company, type, "in")
                outNode = (startVillage, endVillage, company, type, "out")

                revInNode = (endVillage, startVillage, company, type, "in")
                revOutNode = (endVillage, startVillage, company, type, "out")

                masterlist.append(revInNode)
                masterlist.append(revOutNode)
                masterlist.append(inNode)
                masterlist.append(outNode)

                G.add_edge(inNode, outNode, weight=10)
                G.add_edge(revInNode, revOutNode, weight=10)

                if startVillage in vertex_dict:
                    vertex_dict[startVillage].append(inNode)

                else:
                    vertex_dict[startVillage] = [inNode]

                if endVillage in vertex_dict:
                    vertex_dict[endVillage].append(revInNode)
                else:
                    vertex_dict[endVillage] = [revInNode]

            counter += 1

    printdict(vertex_dict)
    print(len(vertex_dict))

    for node in masterlist:
        for node2 in vertex_dict[node[1]]:
            if not(node[0] == node2[1] and node[1] == node2[0]):
                    
                transferTime = calculateTransfer(G, node, node2)
                if not(transferTime is None):
                    G.add_edge(node, node2, weight=transferTime)
                
                


    potentialStarts = vertex_dict[start]
    potentialEnds = []

    for key in vertex_dict:
        for node in vertex_dict[key]:
            if node[1] == end:
                potentialEnds.append(node)

    for node in potentialStarts:
        G.add_edge("pseudoStart", node, weight=0)
    for node in potentialEnds:
        G.add_edge(node, "pseudoEnd", weight=0)

    length, path = nx.single_source_dijkstra(G, source="pseudoStart", target="pseudoEnd")

    truepath = ""

    for node in path:
        if not(node == "pseudoStart" or node == "pseudoEnd"):
            startCity = node[0]
            truepath += startCity + " "

    truepath += endVillage

    print(length)
    print(truepath)

    nx.draw(G, with_labels=True)
    plt.show()




 
def calculateTransfer(G, node1, node2):

    company1 = node1[2]
    company2 = node2[2]
    type1 = node1[3]
    type2 = node2[3]

    if company1 == company2 and type1 == type2: 
        return 0
    elif company1 == company2 and type1 != type2:
        return 2
    elif company1 != company2 and type1 == type2:
        return 5

       


def printdict(dict):
    for cluster in dict:
        print(cluster + " ", end="")
        for node in dict[cluster]:
            print(node[0] + node[1] + " ", end="")
        print()

if __name__ == "__main__":
    main()
