from parse import *
from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 100 ]
edges = []
transform = new_matrix()
parse_file( 'script', edges, transform, screen, color )
# parse_file( 'myscript', edges, transform, screen, color )
