from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, \
    draw_vertical_gradient
import random

def main():
    # Width and height of the scene in pixels.
    scene_width = 800
    scene_height = 500

# Call start_drawing function in draw2d.py library to open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call functions
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)


# Define your functions 
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
        "sky": [(255, 178, 102), (158, 249, 255)],
        "sun": ["sienna1", "salmon2"],
        "cloud": "white",
        "trees": "black"
    }

    if sun_y < 110:
        colors["sky"] = [(39, 41, 72), (1, 2, 32)]
        colors["sun"] = ["sienna1", "salmon2"]
        colors["cloud"] = "lightGray"
        colors["trees"] = "black"
    elif sun_y <= 160:
        colors["sky"] = [(241, 150, 56), (1, 4, 41)]
        colors["sun"] = ["sienna1", "salmon2"]
        colors["cloud"] = "lightGray"
    elif sun_y <= 200:
        colors["sky"] = [(169, 239, 224), (75, 125, 158)]
        colors["sun"] = ["yellow1", "yellow2"]
    elif sun_y <= 250:
        colors["sky"] = [(72, 165, 199), (129, 214, 245)]
        colors["sun"] = ["yellow1", "yellow2"]
    else:
        colors["sky"] = [(72, 165, 199), (129, 214, 245)]
        colors["sun"] = ["yellow1", "yellow2"]

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
    for _ in range(5):
        x_center = random.randint(0, scene_width)
        y_center = random.randint(round(scene_height / 3), scene_height)

        for _ in range(5):
            new_x_center = x_center + random.randint(50, 150)
            new_y_center = y_center - random.randint(15, 25)
            x1 = new_x_center + random.randint(30, 50)
            y1 = new_y_center - random.randint(10, 20)
            x0 = x_center * 2 - x1
            y0 = y_center * 2 - y1
            draw_oval(canvas, x0, y0, x1, y1, width=0, fill=color)


# Define ground and all the items on it.
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width,
        scene_height / 3, width=0, fill="forestGreen")

# Draw trees
    for _ in range(15):
                tree_center_x = random.randint(0, scene_width)
                tree_bottom = random.randint(0, round(scene_height / 3))
                tree_height = 200 * (random.random() + .5)
                if 0 < tree_bottom < 10:
                    draw_pine_tree(canvas, tree_center_x,
                    tree_bottom, tree_height * (random.random() + 1))
                elif 0 < tree_center_x < 200 or 600 < tree_center_x < 800:
                    draw_pine_tree(canvas, tree_center_x,
                    (tree_bottom - 50), tree_height * (random.random() + 1))
                else: 
                    draw_pine_tree(canvas, tree_center_x,
                    tree_bottom, tree_height)

    # # Draw a tree.
    # tree_center_x = 170
    # tree_bottom = 100
    # tree_height = 200
    # draw_pine_tree(canvas, tree_center_x,
    #         tree_bottom, tree_height)



def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
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
#             )


# Call the main function so that
# this program will start executing.
main()