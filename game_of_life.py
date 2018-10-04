import random
import os
from time import sleep


def dead_state(width, height):
    state = []
    for i in range(0, height):
        state.append([" "] * width)
    return state


def random_state(width, height):
    state = dead_state(width, height)
        
    for row in state:
        for cell in range(0, len(row)):
            random_num = random.random()
            if random_num >= 0.5:
                row[cell] = "O"
            else:
                row[cell] = " "

    return state
            
            
def render(state):
    top_and_bottom_border = ("-" * len(state[0])) * 2
    
    print(" " + top_and_bottom_border)
    
    for row in state:
        print("| " + " ".join(map(str, row)) + " |")
            
    print(" " + top_and_bottom_border)


def next_board_state(state):
    is_alive = "O"
    is_dead = " " 
    next_state = []
    
    for row in range(0, len(state)):
        next_state.append([])
        for cell in range(0, len(state[row])):
            alive = 0
            dead = 0
            zombie = False
            cell_state = state[row][cell]

            above = 3    
            above_left = 3
            above_right = 3
            below = 3
            below_left = 3
            below_right = 3
            right = 3
            left = 3
                        
            if row != len(state) - 1 and cell != len(state[row]) - 1:
                below_right = state[row + 1][cell + 1]
            
            if row != 0 and cell != len(state[row]) - 1:
                above_right = state[row - 1][cell + 1]
                
            if row != 0:
                above = state[row - 1][cell]
                above_left = state[row - 1][cell - 1]

            if row != len(state) - 1:
                below = state[row + 1][cell]
                below_left = state[row + 1][cell - 1]
                
            if cell != 0:
                left = state[row][cell - 1]
            
            if cell != len(state[row]) - 1:
                right = state[row][cell + 1]
                            
            if left == is_alive:
                alive += 1
            elif left == is_dead:
                dead += 1
            elif left == "Z":
                zombie = True
                
            if right == is_alive: 
                alive += 1
            elif right == is_dead:
                dead += 1
            elif right == "Z":
                zombie = True
                                
            if above == is_alive:
                alive += 1
            elif above == is_dead:
                dead += 1
            elif above == "Z":
                zombie = True
                                
            if below == is_alive:
                alive += 1
            elif below == is_dead:
                dead += 1
            elif below == "Z":
                zombie = True

            if below_left == is_alive:
                alive += 1
            elif below_left == is_dead:
                dead += 1
            elif below_left == "Z":
                zombie = True

            if below_right == is_alive:
                alive += 1
            elif below_right == is_dead:
                dead += 1
            elif below_right == "Z":
                zombie = True
            
            if above_left == is_alive:
                alive += 1
            elif above_left == is_dead:
                dead += 1
            elif above_left == "Z":
                zombie = True
            
            if above_right == is_alive:
                alive += 1
            elif above_right == is_dead:
                dead += 1
            elif above_right == "Z":
                zombie = True

            if zombie:
                next_state[row].append("Z")
            else:
                                
                if cell_state == is_alive:
                    if alive <= 1 or alive > 3:
                        next_state[row].append(is_dead)
                    
                    if alive in range(2, 4):
                        next_state[row].append(is_alive)

                else:
                    if alive == 3:
                        next_state[row].append(is_alive)   
                    else:
                        random_num = random.random()
                        if random_num >= 0.8:
                            next_state[row].append("Z")
                        else:
                            next_state[row].append(is_dead)
        
    return next_state


init_state = random_state(3, 3)
render(init_state)
new_state = next_board_state(init_state)


while True:
    os.system('cls')
    if new_state == next_board_state(new_state):
        render(new_state)
        break
    else:
        new_state = next_board_state(new_state)
        render(new_state)
        sleep(1)


