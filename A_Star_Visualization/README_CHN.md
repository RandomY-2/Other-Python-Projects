## A* 最短路径可视化

## 介绍 
这个程序通过一个由Pygame模组创建的GUI展示了A*算法如何找到周围有障碍物的两点之间的最短路径。使用者可以通过鼠标左键选择起点和重点和地图上的障碍物。起点将会被标记成橙色，终点会被标记成蓝色
，而障碍会被标记成黑色。当使用者按下空格，这个程序就会开始A*算法的模拟并实时将模拟展现在GUI上。

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
