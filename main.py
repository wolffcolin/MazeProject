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
            prev
            if counter == 0:
                numVillages = int(initialData[0])
                numLines = int(initialData[1])
                start = initialData[2]
                end = initialData[3]
            else:
                startVillage = initialData[0]
                endVillage = initialData[1]

                if len(G.nodes) == 0:
                    G.add_node("" + startVillage + endVillage)
                else:
                    G.add_node("" + startVillage + endVillage)
                    G.

                id = line
                G.add_node(id)

                company = initialData[2]
                type = initialData[3]

                if startVillage not in keyring:
                    vertex_dict[startVillage] = []
                    G.
                vertex_dict[startVillage].append(endVillage)
                    

                ver   tex_dict[startVillage]=endVillage
                keyring.add(startVillage)
            
            counter += 1


    nx.draw(G, with_labels=True)
    plt.show()

    shortest = nx.shortest_path(G, start, end)

if __name__ == "__main__":
    main()

                                                    
