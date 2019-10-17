import numpy_backend as back
import arcade
import numpy as np
import pandas as pd

# Set how many rows and columns we will have
rows = 6
cols = 6

# This sets the WIDTH and HEIGHT of each grid location
width = 50
height = 50
margin = 1

# Do the math to figure out our screen dimensions
screen_width = (width + margin) * cols + margin
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
        self.recreate_grid()
        self.round = 0
        self.last_round_count = [2,2]

    def recreate_grid(self):
        self.shape_list = arcade.ShapeElementList()
        
        print(self.grid)

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

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        self.shape_list.draw()

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
            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                player = (self.round % 2)+1
                self.round += 1

                self.grid[row][column] = player

                back.controller(self.grid, column, row, player)
            else:
                print("not a free spot")
        self.recreate_grid()

def main():
    MyGame(screen_width, screen_height, title)
    arcade.run()

if __name__ == "__main__":
    main()