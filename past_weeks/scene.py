# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    
    

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)


    # draw clouds
    minimum_diameter_size = 30
    maximum_diameter_size = 60
    for i in range(6):
        draw_clouds(canvas, scene_width, minimum_diameter_size, maximum_diameter_size, 600)

    draw_ground(canvas, scene_width, scene_height)

    # draw_pine_tree(canvas, scene_width, scene_height)
    tree_center_x = 600
    tree_bottom = 110
    tree_height = 300
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 690
    tree_bottom = 120
    tree_height = 270
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)


    diameter = 15
    space = 5
    interval = diameter + space

    # draw some random trees
    x = -1
    y = 0
    for i in range(50):
        # number = random.randint(1, 5)
        if x:
            draw_rectangle(canvas, x, y,
                    x + diameter, y + 200, fill="white")
        x += interval

    # Draw some random fences
    x = -10
    y = 0
    for i in range(100):
        number = random.randint(10, 20)
        if x:
            second_y = y + number
            draw_rectangle(canvas, x, y,
                    x + diameter, second_y, fill="green")
        x += interval    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, draw_width, draw_height):
    draw_rectangle(canvas, 0, draw_height / 3,
        draw_width, draw_height, width = 0, fill = "sky blue")

def draw_ground(canvas, draw_width, draw_height):
    draw_rectangle(canvas, 0,0, 
        draw_width, draw_height / 3, width=0, fill = 'tan4')

def draw_clouds(canvas, draw_w, draw_h, max_diam, half_height):
    x = 200
    y = 400
    # diameter = random.randint(min_diam, max_diam)
    draw_oval(canvas, x, y, 2 * x, y + max_diam,
            fill="white")
    x = 250
    y = 375
    # diameter = random.randint(min_diam, max_diam)
    draw_oval(canvas, x, y, 2 * x, y + max_diam,
            fill="white")
    x = 200
    y = 300
    # diameter = random.randint(min_diam, max_diam)
    draw_oval(canvas, x, y, 2 * x, y + max_diam,
            fill="white")

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline = 'gray20', width = 1, fill = 'tan3')

    skirt_w = height / 2
    skirt_h = height - trunk_height
    skirt_l = center_x - skirt_w / 2
    skirt_r = center_x + skirt_w / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top, skirt_r, trunk_top, skirt_l, trunk_top, outline = 'gray20', width = 1, fill = 'dark green')



# Call the main function so that
# this program will start executing.
main()