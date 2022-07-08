import scipy
import numpy as np

def my_agent(observation, configuration):

    class Board:
        """Class representing the ConnectX Board"""

        def __init__(self, level=None, branch=None, parent=None, state=None, n_rows=6, 
                     n_cols=7, game_type=4, win_state=None):

            self.n_rows = n_rows
            self.n_cols = n_cols
            self.game_type = game_type
            self.win_state = win_state
            self.level = level
            self.branch = branch
            self.parent = parent

            if state is None:
                self.state = np.zeros(shape=[self.n_rows, self.n_cols])
            else:
                self.state = state


        def update_board(self, column, player, copy=True):
            """
            Drop the specified player's chip into the chosen column

            column: 0 <= column < n_cols
            player: [1, 2]


            """   

            if copy is False:
                for row, row_val in enumerate(self.state[:, column], 0):
                    if row_val == 0:
    #                     print(f'Player {player}\'s chip dropped onto column {column}, row {row}')
                        self.state[row, column] = player
                        break
            else: 
                state_copy = self.state.copy()
                for row, row_val in enumerate(state_copy[:, column], 0):
                    if row_val == 0:
    #                     print(f'Player {player}\'s chip dropped onto column {column}, row {row}')
                        state_copy[row, column] = player
                        break
                new_board = Board(state=state_copy) # generate new child board with updated state
                new_board.check_win() # check win_state of new board
                return new_board

           # check for win
            if self.check_win() == 1:
                self.win_state = 1 # if true, player 1 won
            elif self.check_win() == 2:
                self.win_state = 2 # if false, player 2 won
            if self.check_draw():
                self.win_state = 3 # if true, board full and draw

        def check_vert_line(self):
            """
            Check if there are 4 connected chips in a vertical line.
            """

            r_lim = self.n_rows - self.game_type  # limit for which row we check till. past the r_lim row, not possible to extend grid vertically up
            for c in range(self.n_cols):
                for r in range(r_lim + 1):
                    cell = self.state[r, c]

                    if cell == 1: # if p1 chip is in [r, c]
                        vert_group = self.state[r:r+4, c] # isolate the 4-cell rectangle extending up from the p1 chip cell
                        if np.all(vert_group == 1): # if all 4 cells have the same value (p1 chip), return win.
    #                         print('Player 1 Wins')
                            self.win_state = 1
                            return None

                    elif cell == 2: # if p2 chip is in [r, c]
                        vert_group = self.state[r: r+4, c] # isolate the 4-cell rectangle extending up from the p1 chip cell
                        if np.all(vert_group == 2): # if all 4 cells have the same value (p1 chip), return win.
    #                         print('Player 2 Wins')
                            self.win_state = 2
                            return None

    #         print('No Vert Lines Found')



        def check_horizontal_line(self):
            """
            Check if there are 4 connected chips in a horizontal line.
            """
            c_lim = self.n_cols - self.game_type # limit for which column we check till. past the c_lim column, not possible to extend grid horizontally to the right
            for c in range(0, c_lim + 1):
                for r in range(self.n_rows):
                    cell = self.state[r, c]

                    if cell == 1: # if p1 chip is in [r, c]
                        hori_group = self.state[r, c:c+4] # isolate the 4-cell rectangle extending up from the p1 chip cell
                        if np.all(hori_group == 1): # if all 4 cells have the same value (p1 chip), return win.
    #                         print('Player 1 Wins')
                            self.win_state = 1
                            return None

                    elif cell == 2: # if p2 chip is in [r, c]
                        hori_group = self.state[r, c:c+4] # isolate the 4-cell rectangle extending up from the p1 chip cell
                        if np.all(hori_group == 2): # if all 4 cells have the same value (p1 chip), return win.
    #                         print('Player 2 Wins')
                            self.win_state = 2
                            return None

    #         print('No Horizontal Lines Found')


        def check_diagonal_line(self):
            """
            Check if there are 4 connected chips in a diagonal line.
            """

            for c in range(self.n_cols):
                for r in range(self.n_rows):
                    cell = self.state[r, c]

                    if cell == 1:
                        # check / diagonals
                        if not (r + 4 >= self.n_rows) and not (c + 4 > self.n_cols):
                            up_right_group = []
                            for i in range(self.game_type):
                                up_right_group.append(self.state[r+i, c+i])
                            up_right_group = np.array(up_right_group)

                            if np.all(up_right_group == 1):
    #                             print('Player 1 Wins')
                                self.win_state = 1
                                return None


                        if not (r - 3 < 0) and not (c + 4 > self.n_cols):
                            down_right_group = []
                            for i in range(self.game_type):
                                down_right_group.append(self.state[r-i, c+i])

                            down_right_group = np.array(down_right_group)

                            if np.all(down_right_group == 1):
    #                             print('Player 1 Wins')
                                self.win_state = 1
                                return None

                    elif cell == 2:
                        # check / diagonals
                        if not (r + 3 >= self.n_rows) and not (c + 4 > self.n_cols):
                            up_right_group = []
                            for i in range(self.game_type):
                                up_right_group.append(self.state[r+i, c+i])
                            up_right_group = np.array(up_right_group)

                            if np.all(up_right_group == 2):
    #                             print('Player 2 Wins')
                                self.win_state = 2
                                return None

                        # check \ diagonals
                        if not (r - 3 < 0) and not (c + 4 > self.n_cols):
                            down_right_group = []
                            for i in range(self.game_type):
                                down_right_group.append(self.state[r-i, c+i])
                            down_right_group = np.array(down_right_group)

                            if np.all(down_right_group == 2):
    #                             print('Player 2 Wins')
                                self.win_state = 2
                                return None

    #         print('No Diagonal Lines Found')

        def check_win(self):
            """
            Check if a player has won.
            """
            self.check_vert_line()
            self.check_horizontal_line()
            self.check_diagonal_line()

            if self.win_state == 1:
    #             print('Player 1 Wins')
                return 1
            elif self.win_state == 2:
    #             print('Player 2 Wins')
                return 2
            else:
                return False

        def check_draw(self):
            """
            Check if the board is full.
            """
            if np.all(self.state != 0):
                return True
            else:
                return False

        def check_full_col(self, column):
            """
            Check if a column is full
            """

            if np.all(self.state[:, column] != 0):
                return True
            else:
                return False
    INFINITY = 9999999999999999999 # yes this is infinity fuck you



    def heuristic_func(current_node):
        """function to calculate the heuristic value of a node"""

        node = Board(state=current_node) # initialise state into a node
        heuristic = 0

        # if board is not in win/lose/draw state, score as follows
        # award points for player 1 chips that are together
        for j in range(node.n_cols):
            for i in range(node.n_rows):

                # check vert lines
                if (i + 2 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == 1:
                    heuristic += 1

                if (i + 3 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == node.state[i+2][j] == 1:
                    heuristic += 5

                if (i + 4 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == node.state[i+2][j] == node.state[i+3][j] == 1:
                    heuristic += 3000

                if (i + 2 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == 2:
                    heuristic -= 1

                if (i + 3 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == node.state[i+2][j] == 2:
                    heuristic -= 50

                if (i + 4 <= node.n_rows) and node.state[i][j] == node.state[i+1][j] == node.state[i+2][j] == node.state[i+3][j] == 2:
                    heuristic -= 10000    

                # check horizontal lines
                if (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == 1:
                    heuristic += 1

                if (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == node.state[i][j+2] == 1:
                    heuristic += 5

                if (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == node.state[i][j+2] == node.state[i][j+3] == 1:
                    heuristic += 3000

                if (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == 2:
                    heuristic -= 1

                if (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == node.state[i][j+2] == 2:
                    heuristic -= 50

                if (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i][j+1] == node.state[i][j+2] == node.state[i][j+3] == 2:
                    heuristic -= 10000

                # check broken horizontals --_- -_--


                if (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i][j+1] == node.state[i][j+3] == 1) and (node.state[i][j+2] == 0):
                    heuristic += 50
                if (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i][j+2] == node.state[i][j+3] == 1) and (node.state[i][j+1] == 0):
                    heuristic += 50

                if (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i][j+1] == node.state[i][j+3] == 2) and (node.state[i][j+2] == 0):
                    heuristic -= 50

                if (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i][j+2] == node.state[i][j+3] == 2) and (node.state[i][j+1] == 0):
                    heuristic -= 50

                # check / diagonal lines
                if (i + 2 <= node.n_rows) and (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == 1:
                    heuristic += 1

                if (i + 3 <= node.n_rows) and (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == node.state[i+2][j+2] == 1:
                    heuristic += 5

                if (i + 4 <= node.n_rows) and (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == node.state[i+2][j+2] == node.state[i+3][j+3] == 1:
                    heuristic += 3000

                if (i + 2 <= node.n_rows) and (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == 2:
                    heuristic -= 1

                if (i + 3 <= node.n_rows) and (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == node.state[i+2][j+2] == 2:
                    heuristic -= 50

                if (i + 4 <= node.n_rows) and (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i+1][j+1] == node.state[i+2][j+2] == node.state[i+3][j+3] == 2:
                    heuristic -= 10000

                # check broken / diagonal lines
                if (i + 4 <= node.n_rows) and (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i+1][j+1] == node.state[i+3][j+3] == 2) and (node.state[i+2][j+2] == 0):
                    heuristic -= 50
                if (i + 4 <= node.n_rows) and (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i+2][j+2] == node.state[i+3][j+3] == 2) and (node.state[i+1][j+1] == 0):
                    heuristic -= 50

                # check \ diagonal lines

                if (i - 1 >= 0) and (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == 1:
                    heuristic += 1

                if (i - 2 >= 0) and (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == node.state[i-2][j+2] == 1:
                    heuristic += 5

                if (i - 3 >= 0) and (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == node.state[i-2][j+2] == node.state[i-3][j+3] == 1:
                    heuristic += 3000

                if (i - 1 >= 0) and (j + 2 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == 2:
                    heuristic -= 1

                if (i - 2 >= 0) and (j + 3 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == node.state[i-2][j+2] == 2:
                    heuristic -= 50

                if (i - 3 >= 0) and (j + 4 <= node.n_cols) and node.state[i][j] == node.state[i-1][j+1] == node.state[i-2][j+2] == node.state[i-3][j+3] == 2:
                    heuristic -= 10000

                # check broken \ diagonal lines
                if (i - 3 >= 0) and (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i-1][j+1] == node.state[i-3][j+3] == 2) and (node.state[i-2][j+2] == 0):
                    heuristic -= 50
                if (i - 3 >= 0) and (j + 4 <= node.n_cols) and (node.state[i][j] == node.state[i-2][j+2] == node.state[i-3][j+3] == 2) and (node.state[i-1][j+1] == 0):
                    heuristic -= 50

        return heuristic

    def minimax(current_node, depth, player=1):
        node = Board(state=current_node) # initialise Board with state of current node

        if depth == 0 or node.check_win() or node.check_draw(): # if at final level of depth, or if node is draw/win/lose (i.e. terminal node)
            value = heuristic_func(node.state)
            return value, -1

        if player == 1: # player 1 is us. we want to maximise our heuristic score
            value = -INFINITY
            max_c = None
            for c in range(node.n_cols):
    #             print(node.check_full_col(c))
                # generate the children of the node 
                if node.check_full_col(c):
                    continue
                elif not node.check_full_col(c):
                    child = node.update_board(column=c, player=1, copy=True)
    #                 print(child.state)
                    child_val, child_c = minimax(child.state, depth-1, player=2)
    #                 print(child_val)
                    if child_val > value: # find the child with max heuristic
                        value = child_val 
                        max_c = c
    #                     print('Player 1')
    #                     print(child.state)
                        print(child_val)
            return value, max_c # return smallest heuristic



        else: # if player 2 (opponent), they want to minimise the heuristic score.
            value = INFINITY
            min_c = None
            for c in range(node.n_cols):
                if node.check_full_col(c):
                    continue
                elif not node.check_full_col(c):
                    child = node.update_board(column=c, player=2, copy=True)
                    child_val, child_c = minimax(child.state, depth-1, player=1)
                    if child_val < value:
                        value = child_val
                        min_c = c
    #                 print('Player 2')
    #                 print(child.state)
    #                 print(child_val)
            return value, min_c
        
    n_rows = configuration['rows']
    n_cols = configuration['columns']
    root_node = np.flipud(np.array(observation['board']).reshape((n_rows, n_cols)))
    # whenever i receive observation, its my turn
    p = observation.mark
    value_of_move, best_move = minimax(root_node, depth=3, player=p) # player 1 wants max heuristic
    print('final', best_move, value_of_move)
    return best_move
