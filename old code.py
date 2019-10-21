

def fill_3(x,y,game_plan,nums):
    if x-y >= 0:
        np.fill_diagonal(game_plan[:,x-y:], nums)
    else:
        np.fill_diagonal(game_plan[y-x:,:], nums)





if index == 1:
            if nums[x+1] == opponent:
                i = 1
                while True:
                    if nums[x+i+1] == opponent and x+i+2 <= len(nums)-1:
                        i += 1
                        continue
                    elif nums[x+i+1] == player:
                        print(index, "Lockin and change to:")
                        while True:
                            nums[x+i] = player
                            if nums[x+i-1] == opponent:
                                i -= 1
                                continue
                            else:
                                break
                        break
            if nums[x-1] == opponent:
                i = 1
                while True:
                    #behövs för senare kriterier
                    if nums[x-i-1] == opponent and x-i-2 >= 0:
                        i += 1
                        continue
                    elif nums[x-i-1] == player:
                        print("Lockin and change to:")
                        # flip
                        while True:
                            nums[x-i] = player
                            if nums[x-i+1] == opponent:
                                i -= 1
                                continue
                            else:
                                break
                    break
            
                    """ if index == 2:
                        print(index, nums)
                        
                        if x-y >= 0:
                            np.fill_diagonal(game_plan[:,x-y:], nums)
                        else:
                            np.fill_diagonal(game_plan[y-x:,:], nums)

                        return game_plan
                    
                    if index == 3:
                        print(index, nums)

                        game_plan_flipped = np.flipud(game_plan)
                        if x-y_new < 0:
                            np.fill_diagonal(game_plan_flipped[y_new-x-1:,:], nums)
                        else:
                            np.fill_diagonal(game_plan_flipped[:,x-y_new+1:], nums)
                        return game_plan               
                        break 
                    break"""