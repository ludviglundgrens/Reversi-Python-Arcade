
import numpy_backend as back
import arcade
import numpy as np

# Set how many rows and columns we will have
rows = 6
cols = 6

# This sets the WIDTH and HEIGHT of each grid location
width = 50
height = 50
margin = 1

# Right margin
right_margin = 100

# Do the math to figure out our screen dimensions
screen_width = (width + margin) * cols + margin + right_margin
screen_height = (height + margin) * rows + margin 
title = "Reversi"

class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)

        self.shape_list = None

        #Create grid from backend
        self.grid = back.create_gameplan()

        # Neccesitys to keep track of game
        arcade.set_background_color(arcade.color.BLACK)
        
        self.round = 0
        self.last_round_grid = self.grid.copy()

        self.recreate_grid()

    def recreate_grid(self):
        self.shape_list = arcade.ShapeElementList()
        
        #print(self.grid)

        for column in range(len(self.grid)):
            for row in range(len(self.grid)):
                if self.grid[rows-row-1][column] == 1:
                    color = arcade.color.WHITE
                elif self.grid[rows-row-1][column] == 2:
                    color = arcade.color.BLACK
                else:
                    color = arcade.color.GREEN

                x = (margin + width) * column + margin + width // 2
                y = (margin + height) * row + margin + height // 2

                current_rect = arcade.create_rectangle_filled(x, y, width, height, color)
                self.shape_list.append(current_rect)

        quit_sprite = arcade.Sprite("quit.png", 0.7)
        pass_sprite = arcade.Sprite("pass.png", 0.7)
        quit_sprite.center_x = 355
        quit_sprite.center_y = 270
        pass_sprite.center_x = 355
        pass_sprite.center_y = 220

        self.button_list = arcade.SpriteList()
        self.button_list.append(quit_sprite)
        self.button_list.append(pass_sprite)
        
        self.quit_sprite_position = quit_sprite.left, quit_sprite.right, quit_sprite.top-quit_sprite.height, quit_sprite.top
        self.pass_sprite_position = pass_sprite.left, pass_sprite.right, pass_sprite.top-pass_sprite.height, pass_sprite.top

        player_1 = arcade.Sprite("player_1.png", 0.5)
        player_2 = arcade.Sprite("player_2.png", 0.5)

        player_1.center_x = 355
        player_1.center_y = 50
        player_2.center_x = 355
        player_2.center_y = 50

        player = (self.round % 2)+1

        if player == 1:
            self.button_list.append(player_1)
        else:
            self.button_list.append(player_2)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        self.shape_list.draw()
        self.button_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (width + margin)
        row = y // (height + margin)

        column = column 
        row = rows-row-1

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist

        if row < rows and column < cols:
            # Flip the location between 1/2 and 0.
            if self.grid[row][column] == 0:
                player = (self.round % 2)+1
                self.round += 1

                self.grid[row][column] = player
                back.controller(self.grid, column, row, player)

                counter_last = count_num(self.last_round_grid)
                counter_new = count_num(self.grid)
                if counter_last[0] < counter_new[0]-1 or counter_last[1] < counter_new[1]-1:
                    print("ok")
                    self.last_round_grid = self.grid.copy()
                else: 
                    print("need to take 1")
                    self.grid = self.last_round_grid.copy()
                    self.round -= 1
            else:
                print("not a free spot")
            self.recreate_grid()
        
        else:
            # båda knapparna är inom detta x
            if self.quit_sprite_position[0] < x < self.quit_sprite_position[1]:
                if self.quit_sprite_position[2] < y < self.quit_sprite_position[3]:
                    print("quit")
                    arcade.close_window()
                elif self.pass_sprite_position[2] < y < self.pass_sprite_position[3]:
                    print("pass")
                    self.round += 1
                    self.recreate_grid()

            print(self.quit_sprite_position)

def count_num(grid):
    counter = [0,0]
    for i in grid:
        for j in i:
            if j == 1:
                counter[0] += 1
            if j == 2:
                counter[1] += 1
    return counter

# class MenuView(arcade.View):
#     def on_show(self):
#         arcade.set_background_color(arcade.color.WHITE)

#     def on_draw(self):
#         arcade.start_render()
#         menu_sprite = arcade.Sprite("menu_view.png", 0.7)
#         menu_sprite.center_x = screen_width / 2
#         menu_sprite.center_y = screen_height / 2
#         menu_sprite.draw()

#         quit_sprite = arcade.Sprite("quit.png", 0.7)
#         quit_sprite.center_x = screen_width / 2
#         quit_sprite.center_y = screen_height / 2 - 100
#         quit_sprite.draw()

#     def on_mouse_press(self, x, y, _button, _modifiers):
#         if y < screen_width/2 - 80:
#             print("quit")
            
#         else:
#             MyGame(screen_width, screen_height, title)
        
        

def main():
    MyGame(screen_width, screen_height, title)
    arcade.run()

if __name__ == "__main__":
    main()
