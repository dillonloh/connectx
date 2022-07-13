# connectx
Minimax algorithm implementation for Connect4 Board game. >=60% win rate against Kaggle env Negamax algorithms.

# Introduction
This notebook was created for the Kaggle ConnectX competition. We attempt to create an agent that is capable of autonomously playing ConnectX (currently only Connect 4)
games, and pit it against the agents created by other users.

# Algorithm (Minimax) description
We implement an adverserial search algorithm called Minimax for our agent. As connectX is a solved game, it is possible for the first player to always force a win. Indeed,
if our trees were deep enough, we could theoretically predict all possible moves by both players within a relatively short amount of time. However, as the competition
limits us to 8 seconds per move, we are limited to either setting a maximum depth for searching, or implementing optimisation techniques like alpha beta pruning.

Our agent works via the following algorithm.

![Tree visualisation](https://miro.medium.com/max/1236/1*IyyCmHRYJpVhkU7SWyuF5Q.png)

Assume that the opponent has just made a move, and the gameboard is now at the state as shown in the top row of the above picture. For each possible move that we can make
(put a chip in either of the 7 columns), we will then check the possible moves that result from each of those new board states. We check through the moves until we reach
a board state that is at our designated maximum search depth, or if it is a terminal board state (either a player has won, or the board is full). This is called a 'decision
tree'. At this point, we apply a 'heuristic function' to these final board states.

Q: What is a heuristic function?
A: A heuristic function is an arbitary function that takes the board as input, and outputs a score. For example, the function may give points for chips of the same colour
that have been put in a row. Typically, we define it in such a way that if the board state is advantageous to player 1 (the main user), it is a positive score, and vice
versa.

After we have scored each of the terminal board states, depending on if the player who made the moves leading to the terminal board states is player 1 or player 2, the
algorithm chooses the move that leads to the maximum/minimum score respectively.

Take the following case:

![Example Decision Tree](https://miro.medium.com/max/556/1*mawaGslmPWazK5oaswgiNQ.png)

Since player 2 was the one making the moves to reach the maximum depth, the algorithm checks which move will lead to the minimum (best score for player 2) score. Then, it will
check which of those moves leads to the maximum score (best score for player 1), and so on and so forth until it goes back up to the original node, where the algorithm
will choose the score that leads to the maximum score. In this way, the algorithm works by ensuring that the best move player 1 makes, is the one that will lead
to the worst moves possible for player 2. 

# Implementation

Minimax pseudo-code:
![Minimax pseudocode](https://miro.medium.com/max/1400/1*JKIe5NUgrZStu8sbgHHjog.png)
Our final agent is a basic Minimax implementation (no pruning), with a search depth of 3. The heuristic function works by checking for the number of each player's chips
that are found lined up vertically, horizontally, and diagonally together. In particular, we assign higher absolute penalties for such lines if they are by player 2, compared to player 1.
This was done with the assumption that we are always player 1.

EDIT: Apparently the kaggle competition sometimes leads to us being player 2, so we should probably flip the above rule in such a case in our update.

4 in a row leads to a score that is much higher than all other scores, hence dominating the heuristic and leading to the algorithm either doing all in its power to work towards it,
or preventing the opponent from winning.

# Results
Against a negamax agent, our agent wins > 60% of games. Attempts at improving the heuristic by adding broken lines as scoring factors (e.g. 11-1, 1-11) etc led to worse
results than without. This needs to be investigated further.

# Conclusions
While the minimax agent worked relatively well (top 100 on Kaggle boards), we could possible increase our maximum depth by implementing pruning to avoid searching through
redundant branches. Similarly, reinforcement learning methods like Q-learning could also be a good choice, especially when the game gets to bigger versions like
Connect 5,6,7 etc. and/or the no. of rows and columns of the board increases (making an adverserial search take too long).




