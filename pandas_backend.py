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
    df = pd.DataFrame(game_plan)
    
    # Första brickor
    df[y/2-1][x/2-1]=1
    df[y/2][x/2]=1

    df[y/2][x/2-1]=2
    df[y/2-1][x/2]=2

    return df

def spela(game_plan, player):
    try:
        print("Spelare", player, "tur att välja kordinater")
        input_str = input("x,y:")
        input_list = input_str.split(",")
        input_list = list(map(int, input_list))
        x = input_list[0]
        y = input_list[1]

        if game_plan[x][y] != 0:
            raise IndexError
        else:
            game_plan[x][y] = player

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
    col = game_plan[x].to_numpy()
    row = game_plan.iloc[y,].to_numpy()

    df_values = game_plan.to_numpy()
    df_flipped = np.flipud(df_values)
    #df_values = game_plan.values
    #df_flipped = np.flipud(df_values)

    diag_1 = df_values.diagonal(x-y).copy()
    #diag_1 = df_values.np.diag(k = (x-y))
    diag_2 = df_flipped.diagonal(-len(df_flipped)+x+y+1).copy()
    #diag_2 = df_flipped.np.diag(k = (-len(df_flipped)+x+y+1))
    
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
            if nums[i] == player and nums[i+1] == opponent and i+2 <= len(nums)-1:
                while True:
                    if nums[i+2] == opponent and i+3 <= len(nums)-1:
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
                            
                            game_plan = game_plan.to_numpy()
                            if x-y >= 0:
                                np.fill_diagonal(game_plan[:,x-y:], nums)
                            else:
                                np.fill_diagonal(game_plan[y-x:,:], nums)
                            game_plan = pd.DataFrame(game_plan)

                            return game_plan
                        
                        if counter == 4:
                            print(counter, nums)
                            game_plan = game_plan.to_numpy()
                            game_plan_flipped = np.flipud(game_plan)

                            #print(game_plan_flipped)
                            y_new = len(game_plan_flipped)-y

                            if x-y_new < 0:
                                np.fill_diagonal(game_plan_flipped[y_new-x-1:,:], nums)
                            else:
                                np.fill_diagonal(game_plan_flipped[:,x-y_new+1:], nums)
                        
                            game_plan = pd.DataFrame(game_plan)

                            return game_plan
                            
                    #elif nums[i+2] == 0:
                        #print("almost Lockin")
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
