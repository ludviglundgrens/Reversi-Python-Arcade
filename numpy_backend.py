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

def modify_num(to_modify, player, game_plan, x, y):
    opponent = find_opponent(player)
    counter = 0
    for nums in to_modify:
        counter += 1
        print(counter, nums)

        # Hitta om det finns "Lockins"
        for i in range(0,len(nums)-1):
            if nums[i] == player and nums[i+1] == opponent and i+3 <= len(nums):
                while True:
                    #behövs för senare kriterier
                    y_new = len(game_plan)-y

                    if nums[i+2] == opponent and i+4 <= len(nums):
                        i += 1
                        continue

                    elif nums[i+2] == player:
                        print("Lockin and change to:")
                        # flip
                        while True:
                            nums[i+1] = player
                            
                            if nums[i] == opponent:
                                i -= 1
                                continue
                            else:
                                break
                        
                        if counter == 3:
                            print(counter, nums)
                            
                            if x-y >= 0:
                                np.fill_diagonal(game_plan[:,x-y:], nums)
                            else:
                                np.fill_diagonal(game_plan[y-x:,:], nums)

                            return game_plan
                        
                        if counter == 4:
                            print(counter, nums)
                            game_plan_flipped = np.flipud(game_plan)

                            if x-y_new < 0:
                                np.fill_diagonal(game_plan_flipped[y_new-x-1:,:], nums)
                            else:
                                np.fill_diagonal(game_plan_flipped[:,x-y_new+1:], nums)
                            return game_plan               
                        break
                    break
        print(counter, nums)
    return game_plan

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
