from edmonds_karp import MaxFlowFinder
from graph_definition.vertex import Vertex
from graph_definition.digraph import Digraph

"""
Run the code
Follow the instructions given in terminal/command line. If You're struggling check README.md file in project
"""
if __name__ == "__main__":
    _end = False
    path = 'adjacency_lists/'
    while not _end:
        print("Please write the name of the graph's adjacency list in format \"graphName.json\".")
        print("Make sure the graphName.json file has been added to /ford-fulkerson/adjacency_lists/ directory.")
        print("You may use the examples already added: \"graph1.json\", \"graph2.json\", \"graph3.json\"")
        try:
            print("json file-name: ")
            source = input()
            graph = Digraph()
            nodes = graph.get_from_file(path + source)
        except:
            try:
                print("Incorrect format. Please try again:")
                print("json file-name: ")
                source = input()
                graph = Digraph()
                nodes = graph.get_from_file(path + source)
            except:
                print("Incorrect format again. Check if .json file exists in /ford-fulkerson/adjacency_lists/ directory. \
Re-run the program and try again.")
                break
        """Uncomment if You wish to draw the graph"""
        # graph.draw(source[0:len(source) - 5] + ".png")
        v1 = Vertex(nodes[0])
        v2 = Vertex(nodes[1])
        algorithm = MaxFlowFinder(graph)
        print("Result maximum flow: " + str(algorithm.edmondsKarpAlgorithm(v1, v2)))
        """Uncomment if You wish to draw the graph with residual edges"""
        # graph.draw(source[0:len(source) - 5] + "_residual.png")
        answer = ""
        while answer != "No" or answer != "Yes":
            print("Do You wish to input another graph? Type: Yes/No : ")
            answer = input()
            if answer == "Yes":
                break
            elif answer == "No":
                print("Goodbye")
                _end = True
                break
