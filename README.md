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
I commented these lines in case there will be any problems with gettings these external libs but feel free to uncomment them if You managed to install requirements.txt.
