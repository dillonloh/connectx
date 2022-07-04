def my_agent(observation, configuration):
#     from random import choice
#     return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    n_rows = configuration['rows']
    n_cols = configuration['columns']
    root_node = np.array(observation['board']).reshape((n_rows, n_cols))
    player = 1 # whenever i receive observation, its my turn
    
    value_of_move, best_move = minimax(root_node, depth=3, player=1) # player 1 wants max heuristic
    
    return best_move
def my_agent(observation, configuration):
#     from random import choice
#     return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    n_rows = configuration['rows']
    n_cols = configuration['columns']
    root_node = np.flipud(np.array(observation['board']).reshape((n_rows, n_cols)))

    player = 1 # whenever i receive observation, its my turn
    
    value_of_move, best_move = minimax(root_node, depth=3, player=1) # player 1 wants max heuristic
    print('final', value_of_move)
    return best_move
def my_agent(observation, configuration):
#     from random import choice
#     return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    n_rows = configuration['rows']
    n_cols = configuration['columns']
    root_node = np.flipud(np.array(observation['board']).reshape((n_rows, n_cols)))

    player = 1 # whenever i receive observation, its my turn
    
    value_of_move, best_move = minimax(root_node, depth=3, player=1) # player 1 wants max heuristic
#     print('final', value_of_move)
    return best_move
def my_agent(observation, configuration):
#     from random import choice
#     return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    n_rows = configuration['rows']
    n_cols = configuration['columns']
    root_node = np.flipud(np.array(observation['board']).reshape((n_rows, n_cols)))

    player = observation.mark # whenever i receive observation, its my turn
    
    value_of_move, best_move = minimax(root_node, depth=3, player=player) # player 1 wants max heuristic
    print('final', best_move, value_of_move)
    return best_move
