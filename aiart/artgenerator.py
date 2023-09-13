import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, \
    draw_vertical_gradient, draw_horizontal_gradient

def main():
    scene_width = 800
    scene_height = 500

    # Call start_drawing function in the draw2d.py to open window and create canvas
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the functions
    draw_sky(canvas, scene_width, scene_height)
    draw_mountain(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    x_center = 500 # change this if you want 0 - 500
    y_center = random.randint(0, 433) # y axis of the sun
    sky_color = get_colors(y_center)["sky"]
    sun_color = get_colors(y_center)["sun"]
    draw_vertical_gradient(canvas, 0, round(scene_height / 3), sky_color[0],
        scene_width, scene_height, sky_color[1])
    x1 = x_center + 67
    y1 = y_center - 67
    x0 = x_center * 2 - x1
    y0 = y_center * 2 - y1
    draw_sun(canvas, x0, y0, x1, y1, sun_color)

def draw_sun(canvas, x0, y0, x1, y1, color):
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill=color)
    draw_oval(canvas, x0 + 5, y0 - 5, x1 - 5, y1 + 5, width=0, fill=color)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    # Midpoint formula ((x0 + x1) / 2, (y0 + y1) / 2)
    # Move sun around using its center coordinates
    x_center = 500 # change this if you want 0 - 500
    y_center = random.randint(0, 433) # y axis of the sun

    # get sky and sun colors depending on the sun's position in the sky
    sky_color = get_colors(y_center)["sky"]
    sun_color = get_colors(y_center)["sun"]
    cloud_color = get_colors(y_center)["cloud"]

    draw_vertical_gradient(canvas, 0, round(scene_height / 3), sky_color[0],
        scene_width, scene_height, sky_color[1])

    x1 = x_center + 67
    y1 = y_center - 67
    x0 = x_center * 2 - x1
    y0 = y_center * 2 - y1
    draw_stars(canvas, scene_width, scene_height, y_center)
    draw_sun(canvas, x0, y0, x1, y1, sun_color[0], sun_color[1])
    draw_clouds(canvas, scene_width, scene_height, cloud_color)


def get_colors(sun_y):
    """Get nature colors depending on the position of the sun."""
    colors = {
        # "sky": [(72, 165, 199), (158, 249, 255)], #blue, light blue
        # "sun": ["sienna1", "salmon2"],
        # "cloud": "white",
        # "ground": [(72, 165, 199), (255, 255, 255)], #blue, white
        "trees": "black",
        # "mount": "gray50"
    }
    if 150 < sun_y <= 250:
        colors["sky"] = [(241, 150, 56), (1, 4, 41)] #blue, light blue
        colors["sun"] = ["yellow1", "yellow2"]
        colors["cloud"] = "gray50"
        colors["ground"] = [(72, 165, 199), (255, 255, 51)] #blue, yellow
        colors["mount"] = "gray50" #[(90, 90, 90), (255, 255, 255)] #dark gray, white
    # elif 100 < sun_y < 150:
    #     colors["sky"] = [(241, 150, 56), (1, 4, 41)] #salmon, dark blue
    #     colors["sun"] = ["sienna1", "salmon2"]
    #     colors["cloud"] = "darkgray"
    #     colors["ground"] = [(75, 125, 158), (241, 150, 56)] #blue, salmon
    #     colors["mount"] = "gray50" #[(90, 90, 90), (255, 255, 255)] #dark gray, white
    elif 0 <= sun_y <= 150:
        colors["sky"] = [(241, 150, 56), (1, 4, 41)] #salmon, dark blue
        colors["sun"] = ["sienna1", "salmon2"]
        colors["cloud"] = "darkgray"
        colors["ground"] = [(1, 4, 41), (241, 150, 56)] #dark blue, salmon
        colors["mount"] = "gray50" #[(90, 90, 90), (255, 255, 255)] #dark gray, white
    else:
        colors["sky"] = [(72, 165, 199), (129, 214, 245)] #blue, light blue
        colors["sun"] = ["yellow1", "yellow2"]
        colors["cloud"] = "white"
        colors["ground"] = [(72, 165, 199), (255, 255, 51)] #blue, yellow
        colors["mount"] = "gray50" #[(90, 90, 90), (255, 255, 255)] #dark gray, white
        colors["trees"] = "black"

    return colors


def draw_stars(canvas, scene_width, scene_height, sun_y):
    if sun_y <= 150:
        for _ in range(500):
            x = random.randint(0, scene_width)
            y = random.randint(round(scene_height / 3), 500)
            draw_oval(
                canvas,
                x, y,
                x + 1, y - 1,
                outline="lightBlue", fill="lightBlue"
            )


def draw_sun(canvas, x0, y0, x1, y1, color1, color2):
    """Draw sun on canvas."""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill=color1)
    draw_oval(canvas, x0 + 5, y0 - 5, x1 - 5, y1 + 5, width=0, fill=color2)


def draw_clouds(canvas, scene_width, scene_height, color):
    for _ in range(random.randint(0, 12)):
        x_center = random.randint(0, scene_width)
        y_center = random.randint(round(scene_height / 3), scene_height)

        for _ in range(random.randint(0, 12)):
            new_x_center = x_center + random.randint(50, 150)
            new_y_center = y_center - random.randint(5, 25)
            x1 = new_x_center + random.randint(5, 100)
            y1 = new_y_center - random.randint(5, 25)
            x0 = x_center * 2 - x1
            y0 = y_center * 2 - y1
            draw_oval(canvas, x0, y0, x1, y1, width=0, fill=color)

def draw_ground(canvas, scene_width, scene_height):
    x_center = 500 # change this if you want 0 - 500
    y_center = random.randint(0, 433) # y axis of the sun
    
    ground_color = get_colors(y_center)["ground"]
    # trees_color = get_colors(y_center)["trees"]

    draw_horizontal_gradient(canvas, 0, 0, ground_color[0],
        500, round(scene_height / 3), ground_color[1])
    draw_horizontal_gradient(canvas, 500, 0, ground_color[1],
        scene_width, round(scene_height / 3), ground_color[0])
    
    # for _ in range(150):
    #             tree_center_x = random.randint(0, scene_width)
    #             tree_bottom = random.randint(200, 300)
    #             tree_height = 20 * (random.random() + .5)
    #             if 0 < tree_bottom < 10:
    #                 draw_pine_tree(canvas, tree_center_x,
    #                 tree_bottom, tree_height * (random.random() + 1))
    #             # elif 0 < tree_center_x < 200 or 600 < tree_center_x < 800:
    #             #     draw_pine_tree(canvas, tree_center_x,
    #             #     (tree_bottom - 50), tree_height * (random.random() + 1))
    #             else: 
    #                 draw_pine_tree(canvas, tree_center_x,
    #                 tree_bottom, tree_height)

    # draw_rectangle(canvas, 0, 0,
    #     scene_width, scene_height / 3, width=0, fill=ground_color)
    # draw_trees(canvas, scene_width, scene_height, trees_color)

    # # Draw a pine tree.
    # tree_center_x = random.randint(0, scene_width)
    # tree_bottom = random.randint(0, scene_width)
    # tree_height = random.randint(0, scene_width)
    # draw_pine_tree(canvas, tree_center_x,
    #         tree_bottom, tree_height)

    # # Draw another pine tree.
    # tree_center_x = 90
    # tree_bottom = 70
    # tree_height = 220
    # draw_pine_tree(canvas, tree_center_x,
    #         tree_bottom, tree_height)

    # # Draw another pine tree.
    # tree_center_x = 590
    # tree_bottom = 70
    # tree_height = 300
    # draw_pine_tree(canvas, tree_center_x,
    #         tree_bottom, tree_height)
    
    # # Draw another pine tree.
    # tree_center_x = 710
    # tree_bottom = 50
    # tree_height = 350
    # draw_pine_tree(canvas, tree_center_x,
    #         tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height, scene_width, scene_height, sun_y):
    """
    Parameters to draw a single pine tree.
        canvas: The canvas where this function will draw a pine tree.
        center_x, bottom: The x and y location in pixels where this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

# def draw_trees(canvas, scene_width, scene_height, sun_y):
#     if sun_y <= 150:
#         for _ in range(500):
#             x = random.randint(0, scene_width)
#             y = random.randint(round(scene_height / 3), 500)
#             draw_pine_tree(
#                 canvas,
#                 x, y,
#                 x + 1, y - 1,
#                 outline="lightBlue", fill="lightBlue"
            # )

def draw_mountain(canvas, scene_width, scene_height):
    x_center = 500 # change this if you want 0 - 500
    y_center = random.randint(0, 433) # y axis of the sun

    mount_color = get_colors(y_center)["mount"]
    # draw_vertical_gradient(canvas, 0, round(scene_height / 3), mount_color[0],
    #     scene_width, scene_height, mount_color[1])

    # for _ in range(random.randint(0, 12)):
    #     x_center = random.randint(0, scene_width)
    #     y_center = random.randint(200, 300)

    #     for _ in range(random.randint(0, 12)):
    #         new_x_center = x_center + random.randint(50, 150)
    #         new_y_center = y_center - random.randint(5, 25)
    #         x1 = new_x_center + random.randint(5, 100)
    #         y1 = new_y_center - random.randint(5, 25)
    #         x0 = x_center * 2 - x1
    #         y0 = y_center * 2 - y1
    #         ccolor = ('gray80')
    #         draw_oval(canvas, x0, y0, x1, y1, width=0, fill=ccolor)

    center_x = 500
    mt_width = scene_height * 3
    mt_height = scene_height - 100
    mt_left = center_x - mt_width / 2
    mt_right = center_x + mt_width / 2
    mt_top = scene_height / (random.random() + 1.2)

    draw_polygon(canvas, center_x, mt_top,
            mt_right, 100,
            mt_left, 100,
            outline="gray20", width=1, fill=mount_color)

    center_x = 200
    mt_width = scene_height * 3
    mt_height = scene_height
    mt_left = center_x - mt_width / 4
    mt_right = center_x + mt_width / 2
    mt_top = scene_height / (random.random() + 1.25)

    draw_polygon(canvas, center_x, mt_top,
            mt_right, 100,
            mt_left, 100,
            outline="gray20", width=1, fill=mount_color)

    # for _ in range(random.randint(0, 4)):
    #     x_center = random.randint(0, scene_width)
    #     y_center = random.randint(200, 300)

    #     for _ in range(random.randint(0, 4)):
    #         new_x_center = x_center + random.randint(50, 150)
    #         new_y_center = y_center - random.randint(5, 25)
    #         x1 = new_x_center + random.randint(5, 100)
    #         y1 = new_y_center - random.randint(5, 25)
    #         x0 = x_center * 2 - x1
    #         y0 = y_center * 2 - y1
    #         ccolor = ('gray80')
    #         draw_oval(canvas, x0, y0, x1, y1, width=0, fill=ccolor)
    
    center_x = 350
    mt_width = scene_height * 3
    mt_height = scene_height
    mt_left = center_x - mt_width / 4
    mt_right = center_x + mt_width / 2
    mt_top = scene_height / (random.random() + 1.75)

    draw_polygon(canvas, center_x, mt_top,
            mt_right, 100,
            mt_left, 100,
            outline="gray20", width=1, fill='gray50')

    for _ in range(random.randint(0, 4)):
        x_center = random.randint(0, scene_width)
        y_center = random.randint(200, 300)

        for _ in range(random.randint(0, 4)):
            new_x_center = x_center + random.randint(50, 150)
            new_y_center = y_center - random.randint(5, 25)
            x1 = new_x_center + random.randint(5, 100)
            y1 = new_y_center - random.randint(5, 25)
            x0 = x_center * 2 - x1
            y0 = y_center * 2 - y1
            ccolor = ('gray80')
            draw_oval(canvas, x0, y0, x1, y1, width=0, fill=ccolor)

    center_x = 420
    mt_width = scene_height * 5.5
    mt_height = scene_height
    mt_left = center_x - mt_width / (random.random() + 1.2)
    mt_right = center_x + mt_width / (random.random() + 1.5)
    mt_top = scene_height / 2.5

    draw_polygon(canvas, center_x, mt_top,
            mt_right, 100,
            mt_left, 100,
            outline="gray20", width=1, fill='gray40')

# Call the main function to execute program
if __name__ == "__main__":
    main()