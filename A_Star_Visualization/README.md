## A* Shortest Path Visualization

[中文版](https://github.com/RandomY-2/Python-GUI-Games/blob/main/A_Star_Visualization/README_CHN.md)


## Description 
This program illustrates how A* algorithm finds the shortest path between two points. The user can select the start and end points and can create the barriers on the map. Then, 
when the user presses space, A* algorithm will run and the GUI will show how it is finding the path between the two points while taking the barriers into consideration. The first 
point user clicks will be the start point, which is marked orange, and the second point clicked is the end point, which is marked blue. Then the user can create barriers that 
are colored black. Finally, the user can hit space to see how A* finds the shortest path.

## A* Shortest Path Finding Algorithm
A* searching algorithm is an advanced path finding algorithm which knows the general direction it should be looking toward when finding the shortest path between two points. This
allows the algorithm to find the path quicker than other traversing algorithms like BFS or DFS or even dijkstra.

What A* does is that during each visit, the algorithm picks a node that has the lowest **F** value, which equals to the sum of another two values - **G** and **H**. The **G** and 
**H** values are determined as follows:
  - **G** is the cost to move from the start point to the current location following the path generated to get there. 
  - **H** is the cost to move from the current location to the final destination. (Most of the time this is really just a smart guess)

## A View of the program:

<p align="center">
  <img width="700" height="800" src="https://github.com/RandomY-2/Python-GUI-Games/blob/main/A_Star_Visualization/images/sample.jpg">
</p>
