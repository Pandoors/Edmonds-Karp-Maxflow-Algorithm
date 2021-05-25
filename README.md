# Ford-Fulkerson's method of finding the maximum flow in graph with Edmonds Karp algorithm approach.

This program searches for the maximum flow of the graph. I described every method, class and function in code.

# If You don't want to draw graphs:

1) To run this code - firstly - simply download zip, or clone this repository using git:
```
git clone https://github.com/Pandoors/Edmonds-Karp-Maxflow-Algorithm
```

2) Then go to project directory and simply run the main.py
```
python3 main.py
```

# If You want to draw graphs:

Follow the previously written step 1) and then download the requirements.txt. As You have them downloaded:

Uncomment line 33, 39 in main.py in projects.
These lines:
```
        """Uncomment if You wish to draw the graph"""
        # graph.draw(source[0:len(source) - 5] + ".png")

```
and
```
      """Uncomment if You wish to draw the graph with residual edges"""
        # graph.draw(source[0:len(source) - 5] + "_residual.png")
```

Then the graph images will be saved in networkx_files directory. I already draw the examples.
I commented these lines in case there will be any problems with gettings these external libs but feel free to uncomment them if You managed to install requirements.txt. There is no need at all to install requirements in case You keep those lines commented.

# How program gives results
results are being printed in the console during working of the program. Every time algorithm finds the path it prints it. Also prints the minimum fow of edges that has to be substracted from edges in path and actual max-flow of the graph. For example:
```
printing path: ( 0 )->( 1 )->( 2 )->( 4 )->( 3 )->( 5 )->( 6 )
actual minimum flow of edges: 1
actual maximum flow of graph: 5
```
Then it prints the actual Graph edges with residual edges flow, for example: 
```
Graph edges: 
( 0 --> 1 ) with weigh: 3 with flow: 3 with remaining flow: 1
( 0 --> 3 ) with weigh: 3 with flow: 3 with remaining flow: 0
( 1 --> 2 ) with weigh: 4 with flow: 4 with remaining flow: 2
( 2 --> 0 ) with weigh: 3 with flow: 3 with remaining flow: 3
( 2 --> 3 ) with weigh: 1 with flow: 1 with remaining flow: 0
( 2 --> 4 ) with weigh: 2 with flow: 2 with remaining flow: 1
( 3 --> 4 ) with weigh: 2 with flow: 2 with remaining flow: 2
( 3 --> 5 ) with weigh: 6 with flow: 6 with remaining flow: 2
( 4 --> 1 ) with weigh: 1 with flow: 1 with remaining flow: 1
( 4 --> 6 ) with weigh: 1 with flow: 1 with remaining flow: 0
( 5 --> 6 ) with weigh: 9 with flow: 9 with remaining flow: 5
( 3 --> 0 ) residual edge with remaining flow: 3
( 4 --> 3 ) residual edge with remaining flow: 0
( 6 --> 4 ) residual edge with remaining flow: 1
( 5 --> 3 ) residual edge with remaining flow: 4
( 6 --> 5 ) residual edge with remaining flow: 4
( 1 --> 0 ) residual edge with remaining flow: 2
( 2 --> 1 ) residual edge with remaining flow: 2
( 3 --> 2 ) residual edge with remaining flow: 1
( 4 --> 2 ) residual edge with remaining flow: 1
```
At the end of working, when there is no edge left, the program prints the maximum flow of graph, for example:
```
Result maximum flow: 5
```
