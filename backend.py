
# Setup
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

def create_gameplan():
    game_plan = []
    for i in range(7):
        game_plan.append([])
        for j in range(7):
                game_plan[i].append(0)
                j = j
    return game_plan

def spela(game_plan, player):
    input_str = input("x,y: ")
    input_list = input_str.split(",")
    input_list = list(map(int, input_list))
    x = input_list[0]-1
    y = input_list[1]-1

    # find if it is next to opposite sort
    controller(game_plan, x, y, player)

    game_plan[y][x] = player

def opponent(player):
    if player == 1:
        return 2
    else:
        return 1

def controller(game_plan, x, y, player):
    #Första delen av kontroll
    offset_value = []
    for offset in offsets:
        a = offset[0]
        b = offset[1]
        offset_value.append(game_plan[y+b][x+a])
    #print(offset_value)

    # Andra delen
    print(game_plan[x][y:])
    print(game_plan[x][0:y])

    over = []
    under = []
    for i in range(x, len(game_plan)):
        under.append(game_plan[i][x])
    print(under)
    for i in range(0,x):
        over.append(game_plan[i][x])
    print(over)
    #print(game_plan[0:x])
a

    

def print_gameplan(game_plan):
    for i in game_plan:
        print(*i)

def main():
    game_plan = create_gameplan()

    i = 0
    while i < 10:
        player = (i % 2)+1
        spela(game_plan=game_plan, player = player)
        print_gameplan(game_plan=game_plan)
        i += 1

main()

