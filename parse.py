from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    f = f.read().splitlines()
    for index in range(0, len(f)):
        if f[index] == "line":
            index += 1
            edges = f[index].split(" ")
            add_edge( points, int(edges[0]), int(edges[1]), int(edges[2]), int(edges[3]), int(edges[4]), int(edges[5]) )
        if f[index] == "ident":
            ident(transform)
        if f[index] == "scale":
            index += 1
            new = f[index].split(" ")
            change = make_scale(int(new[0]), int(new[1]), int(new[2]))
            matrix_mult(change, transform)
        if f[index] == "move":
            index += 1
            new = f[index].split(" ")
            change = make_translate(int(new[0]), int(new[1]), int(new[2]))
            matrix_mult(change, transform)
        if f[index] == "rotate":
            # print("rotate")
            index += 1
            new = f[index].split(" ")
            change = []
            if new[0] == "x":
                change = make_rotX(int(new[1]))
            if new[0] == "y":
                change = make_rotY(int(new[1]))
            if new[0] == "z":
                change = make_rotZ(int(new[1]))
            matrix_mult(change, transform)
        if f[index] == "apply":
            matrix_mult(transform, points)
        if f[index] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        if f[index] == "save":
            clear_screen(screen)
            draw_lines(points,screen,color)
            index += 1
            save_ppm(screen,f[index])
        if f[index] == "quit":
            break
        # index += 1
    #     print line
