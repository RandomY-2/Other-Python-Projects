## Minimax 井字游戏

## 介绍 
这个游戏是一个基于Python Tkinder包进行绘制的井字游戏。玩家将会和一个通过Minimax算法编程的电脑对手进行游戏。当使用者运行这个游戏，一个展示井字格的GUI将会被绘制。使用者会执X，电脑
对手将会执O。当游戏的结果确定了之后，程序会展现一个对话框来告诉使用者游戏结果（赢/输/平局）。当玩家尝试进行违规操作（如试图在已经落子的格子放X），一个warning对话框会被展示并要求
玩家重新开始游戏。

## Minimax 算法
Minimax算法又名极小化极大算法，是一种找出失败的最大可能性中的最小值的算法。程序将会假设对手每一步都会进行对对方最优的策略（即对我方价值最小的格局）。因此Minimax会让程序选择那些对方
所能达到的让我方最差情况中最好的，也就是让对方在完美决策下所对我造成的损失最小

is a recursive backtracking algorithm that is used in game theory to find the most optimal move. The algorithm assumes that the opponent always plays most optimally, 
and the algorithm will find what action leads to the best outcome in this sense. For this game, the minimax algorithm is implemented so that the program will play the move that
can lead to best game result (win > tie > lose).

## A View of the game:

<p align="left">
  <img width="300" height="500" src="https://github.com/RandomY-2/Python-GUI-Games/blob/main/TicTacToe/images/GameImage.jpg">
  <img width="300" height="500" src="https://github.com/RandomY-2/Python-GUI-Games/blob/main/TicTacToe/images/Warning_cheating.jpg">
  <img width="300" height="500" src="https://github.com/RandomY-2/Python-GUI-Games/blob/main/TicTacToe/images/Wining.jpg">
</p>
