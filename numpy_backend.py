import pandas as pd
import numpy as np

x = 6
y = 6

def create_gameplan():
    game_plan = []
    for i in range(y):
        game_plan.append([])
        for j in range(x):
                game_plan[i].append(0)
                j = j

    game_plan = np.array(game_plan)

    # Första brickor
    game_plan[int(y/2-1)][int(x/2-1)]=1
    game_plan[int(y/2)][int(x/2)]=1

    game_plan[int(y/2)][int(x/2-1)]=2
    game_plan[int(y/2-1)][int(x/2)]=2

    return game_plan

def spela(game_plan, player):
    try:
        print("Spelare", player, "tur att välja kordinater")
        input_str = input("x,y:")
        input_list = input_str.split(",")
        input_list = list(map(int, input_list))
        x = input_list[0]
        y = input_list[1]

        if game_plan[y][x] != 0:
            raise IndexError
        else:
            game_plan[y][x] = player

        # Controll if value is ok
        game_plan = controller(game_plan, x,y, player)
        
    except ValueError:
        print("Välj kordinat på spelplanen: (x,y). Till exempel: 3,4")
        spela(game_plan = game_plan, player = player)
    except IndexError:
        print("Felaktigt format på kordinater. Till exempel: 3,4")
        spela(game_plan = game_plan, player = player)
    
    return game_plan

def controller(game_plan, x,y, player):
    col = game_plan[:,x]
    row = game_plan[y,:]
    game_plan_flipped = np.flipud(game_plan)

    diag_1 = game_plan.diagonal(x-y).copy()
    diag_2 = game_plan_flipped.diagonal(-len(game_plan_flipped)+x+y+1).copy()
    
    to_modify = [col, row, diag_1, diag_2]
    game_plan = modify_num(to_modify, player, game_plan, x, y)

    return game_plan

def find_opponent(player):
    if player == 1:
        return 2
    else:
        return 1

def fill_simple(y,nums,opponent,player,index):
    if y+1 < len(nums) and len(nums) > 2:
        if nums[y+1] == opponent and y+3 < len(nums):
            i = 1
            while True:
                if nums[y+i+1] == opponent and y+i+2 < len(nums):
                    i += 1
                    continue
                elif nums[y+i+1] == player:
                    print(index, "Lockin and change to:")
                    while True:
                        nums[y+i] = player
                        if nums[y+i-1] == opponent:
                            i -= 1
                            continue
                        else:
                            break
                    print(index,nums)
                break
    if nums[y-1] == opponent and len(nums) > 2 and y-2 >= 0:
            i = 1
            while True:
                #behövs för senare kriterier
                if nums[y-i-1] == opponent and y-i-2 >= 0:
                    i += 1
                    continue
                elif nums[y-i-1] == player:
                    print("Lockin and change to:")
                    # flip
                    while True:
                        nums[y-i] = player
                        if nums[y-i+1] == opponent:
                            i -= 1
                            continue
                        else:
                            break
                    print(nums)
                break
    return nums

def modify_num(to_modify, player, game_plan, x, y):
    opponent = find_opponent(player)
    for index, nums  in enumerate(to_modify):
        print(index, nums)
        if index == 0:
            fill_simple(y,nums,opponent,player,index)
        if index == 1:
            fill_simple(x,nums,opponent,player,index)
        if index == 2:
            if x-y >= 0:
                placing = y
            else:
                placing = x
            new_nums = fill_simple(placing, nums, opponent, player, index)
            print(new_nums)
            #fyll diagonalt
            if x-y >= 0:
                np.fill_diagonal(game_plan[:,x-y:], new_nums)
            else:
                np.fill_diagonal(game_plan[y-x:,:], new_nums)
        if index == 3:  
            y_inv = len(game_plan)-y-1
            if x-y_inv >= 0:
                placing = y_inv
            else:
                placing = x
            new_nums = fill_simple(placing, nums, opponent, player, index)
            print(new_nums)
            #fyll diagonalt
            game_plan_flipped = np.flipud(game_plan)
            if x-y_inv >= 0:
                np.fill_diagonal(game_plan_flipped[:,x-y_inv:], nums)
            else:
                np.fill_diagonal(game_plan_flipped[y_inv-x:,:], nums)
            return game_plan      

    return game_plan

def count_num(grid):
    counter = [0,0]
    for i in grid:
        for j in i:
            if j == 1:
                counter[0] += 1
            if j == 2:
                counter[1] += 1
    return counter       

def main():
    game_plan = create_gameplan()
    print(game_plan)
    i = 0
    while i >= 0:
        player = (i % 2)+1
        game_plan = spela(game_plan, player)
        print(game_plan)
        i += 1

if __name__ == "__main__":
    main()
