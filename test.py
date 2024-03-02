import random
import math

def count_collisions(state):
    collisions = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                collisions += 1
    return collisions

def solve():
    state = [random.randint(0, 3) for _ in range(4)]
    temp = 1000
    while temp > 0:
        next_state = state[:]
        next_state[random.randint(0, 3)] = random.randint(0, 3)
        if count_collisions(next_state) < count_collisions(state) or random.random() < math.exp((count_collisions(state) - count_collisions(next_state)) / temp):
            state = next_state
        temp -= 1
    return state

print(solve())
