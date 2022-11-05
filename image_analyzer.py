from PIL import Image
import numpy as np

class Pixel():
    def __init__(self,RGB) -> None:
        self.r = RGB[0]
        self.g = RGB[1]
        self.b = RGB[2]
        self.energy = 0
        self.path_costs = 0
    
    def getRGB(self):
        return [self.r, self.g, self.b]
    
    def __repr__(self):
        return str(self.path_costs)
    
    def __lt__(self,other):
        return self.path_costs < other.path_costs
        
    def __eq__(self,other):
        return self.path_costs == other.path_costs

    def __gt__(self,other):
        return self.path_costs > other.path_costs

#calculate RGB energy
    def calc_energy(self,neighbors):
        for pixel in neighbors:
            self.energy += self - pixel
        self.energy /= len(neighbors)

#Dunder Method
    def __sub__(self,other):
        return abs(self.r - other.r) + abs(self.g - other.g) + abs(self.b - other.b)

    def __str__(self) -> str:
        if self.r > self.g and self.r > self.b:
            return 'R'
        if self.g > self.r and self.g > self.b:
            return 'G'
        if self.b > self.r and self.b > self.g:
            return 'B'
        return 'W'

#Create the pixel map
def create_pixel_map(image):
    pixel_map = []
    for row in range(image.height):
        pixel_row = []
        for col in range(image.width):
            pixel_row.append(Pixel(image.getpixel((col,row))))
        pixel_map.append(pixel_row)
    return pixel_map

#Get neighboring pixels in the row/cols.
def get_neighbors_of_pixel(pixel_map,pixel_row,pixel_col):
    neighbors = []
    for row in range(pixel_row - 1, pixel_row + 2):
        for col in range(pixel_col - 1, pixel_col + 2):
            if row >= 0 and row < len(pixel_map) and col >= 0 and col < len(pixel_map[0]) and (pixel_row != row or pixel_col != col):
                neighbors.append(pixel_map[row][col])
    return neighbors

def calculate_energies(pixel_map):
    for row in range(len(pixel_map)):
        for col in range(len(pixel_map[row])):
            pixel_map[row][col].calc_energy(get_neighbors_of_pixel(pixel_map,row,col))
    return pixel_map

#Open the image
def show_image(filename):
    image = Image.open(filename)
    image.show()

def show_pixels(image):
    pixel_array = []
    for row in range(image.height):
        pixel_row = []
        for col in range(image.width):
            pixel_row.append(image.getpixel((col, row)))
        pixel_array.append(pixel_row)
    return pixel_array

#Print a pixel map.
def print_pixels(pixel_map):
    for row in range(len(pixel_map)):
        current_row = []
        for col in range(len(pixel_map[row])):
            current_row.append(str(pixel_map[row][col]))
        print(current_row)

#Generate the energy from pixels
def print_energies(pixel_map):
    for row in range(len(pixel_map)):
        current_row = []
        for col in range(len(pixel_map[row])):
            current_row.append(pixel_map[row][col].energy)
        print(current_row)

#Output path costs
def print_path_costs(pixel_map):
    for row in range(len(pixel_map)):
        current_row = []
        for col in range(len(pixel_map[row])):
            current_row.append(pixel_map[row][col].path_costs)
        print(current_row)

#Find the parent pixels
def get_parent_pixels(pixel_map, row, col):
    parent_pixels = []
    parent_pixels.append(pixel_map[row - 1][col])
    if col > 0:
        parent_pixels.append(pixel_map[row - 1][col - 1])
    if col < len(pixel_map[row]) - 1:
        parent_pixels.append(pixel_map[row - 1][col + 1])
    return parent_pixels

#Get the path costs
def calculate_path_costs(pixel_map):
    for col in range(len(pixel_map[0])):
        pixel_map[0][col].path_costs = pixel_map[0][col].energy
    for row in range(1,len(pixel_map)):
        for col in range(len(pixel_map[row])):
            pixel_map[row][col].path_costs = pixel_map[row][col].energy + min(get_parent_pixels(pixel_map,row,col)).path_costs

#Find the lowest path.
def get_lowest_path(pixel_map):
    lowest_col = pixel_map[-1].index(min(pixel_map[-1]))
    path = []
    path.append(lowest_col)
    for row in range(len(pixel_map) - 1, 0, -1):
        lowest_col = get_lowest_col(pixel_map,row,lowest_col)
        path.append(lowest_col)
    path.reverse()
    return path

#Find the lowest column from its parent pixels.
def get_lowest_col(pixel_map,row,col):
    # print('Found ', pixel_map[row - 1], 'in', min(get_parent_pixels(pixel_map,row - 1,col)).path_costs)
    return pixel_map[row - 1].index(min(get_parent_pixels(pixel_map,row,col)), max(0, col - 1), min(col + 2, len(pixel_map[row])))

#Find the lowest RGB path.
def color_path(image, path):
    for row in range(image.height):
        image.putpixel([path[row], row], (255, 0, 0))

#Remove it.
def remove_path(pixel_map, path):
    for row in range(len(pixel_map)):
        pixel_map[row].pop(path[row])

#Create a new image with the changes.
def create_image(pixel_map):
    image_array = []
    for row in range(len(pixel_map)):
        current_row = []
        for col in range(len(pixel_map[row])):
            current_row.append(pixel_map[row][col].getRGB())
        image_array.append(current_row)
    image_array = np.asarray(image_array)
    image_array = np.uint8(image_array)
    image = Image.fromarray(image_array)
    image.save('tree_trimmed.png')
    
file = 'tree.png'
image = Image.open(file)
# pixel_array = show_pixels(image)
# for row in pixel_array:
#     print(row)


pixel_map = create_pixel_map(image)
columns_to_remove = 20
for x in range(columns_to_remove):
    calculate_energies(pixel_map)
    calculate_path_costs(pixel_map)
    path = get_lowest_path(pixel_map)
    remove_path(pixel_map, path)
create_image(pixel_map)


# calculate_energies(pixel_map)

# calculate_path_costs(pixel_map)
# # print_pixels(pixel_map)
# # print_path_costs(pixel_map)

# get_lowest_path(pixel_map)

# color_path(image, get_lowest_path(pixel_map))
# image.show()
# print()


# show_image(file)
# show_image('person.png')