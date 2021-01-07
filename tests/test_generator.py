import sys

args = sys.argv[1:]
grid_width, grid_height = args
grid_width = int(grid_width)
grid_height = int(grid_height)
distance: float = 1.6

with open(f'input_{grid_height * grid_width}.txt', 'w') as f:
    for i in range(grid_height):
        for j in range(grid_width):
            f.write(f'{distance * j} {distance * i}\n')
