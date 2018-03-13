from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    t = 0.0
    px = cx + r
    py = cy
    while (t <= 1.0):
        theta = 2 * math.pi * t
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        add_edge(points, x, y, 0, px, py, 0)
        px = x
        py = y
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x_coefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    y_coefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    t = 0.0
    px = x0
    py = y0
	#print x_coefs[0][0]
    while (t <= 1.0):
		x = x_coefs[0][0] * t ** 3 + x_coefs[0][1] * t ** 2 + x_coefs[0][2] * t + x_coefs[0][3]
		y = y_coefs[0][0] * t ** 3 + y_coefs[0][1] * t ** 2 + y_coefs[0][2] * t + y_coefs[0][3]
		add_edge(points, x, y, 0, px, py, 0)
		t += step
		px = x
		py = y
		#print i


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    for c in range(0, len(matrix[0]), 2):
        draw_line(matrix[0][c],matrix[1][c], matrix[0][c+1], matrix[1][c+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
