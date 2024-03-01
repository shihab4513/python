import random
import math

def get_number_of_collisions(arr):
    # Calculate the total number of attacking pairs (row attacks, column attacks, and diagonal attacks)
    collisions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] or abs(arr[i] - arr[j]) == j - i:
                collisions += 1
    return collisions

def get_evaluation(arr):
    # Return the negative value of the number of collisions
    return -get_number_of_collisions(arr)

def hill_climbing_simulated_annealing():
    # Initialize the board with 4 queens randomly placed in each row
    board = [random.randint(0, 3) for _ in range(4)]
    temperature = 1000
    cooling_rate = 1

    while temperature > 0:
        # Generate a neighboring state by moving a queen
        row = random.randint(0, 3)
        new_col = random.choice([board[row] - 1, board[row] + 1]) % 4
        new_board = board[:row] + [new_col] + board[row + 1:]

        # Calculate evaluation scores
        current_eval = get_evaluation(board)
        new_eval = get_evaluation(new_board)

        # Decide whether to accept the new state
        if new_eval >= current_eval or random.uniform(0, 1) <= math.exp((new_eval - current_eval) / temperature):
            board = new_board

        # Decrease temperature
        temperature -= cooling_rate

    return board

# Solve the 4-queens problem
best_solution = hill_climbing_simulated_annealing()
print("Best solution (column positions of queens):", best_solution)
