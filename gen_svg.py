#!/usr/bin/env python

import sys
from math import sin,cos,pi
import kolakoski as klk

def print_svg_sector(f,x,y,color,r,th,dr,dth):
    # set initial angle to 0
    final_th = th*180/pi - 360
    th = 0

    maxr = r+dr/2
    minr = r-dr/2
    
    maxth = th+dth/2
    minth = th-dth/2
    
    # 4 corners of sector centered at r,th
    # with widths dr,dth
    x1 = x + minr*cos(minth)
    y1 = y + minr*sin(minth)

    x2 = x + maxr*cos(minth)
    y2 = y + maxr*sin(minth)

    x3 = x + maxr*cos(maxth)
    y3 = y + maxr*sin(maxth)

    x4 = x + minr*cos(maxth)
    y4 = y + minr*sin(maxth)

    print("""<path fill=\"{}\" stroke=\"{}\"
            d=\"
            M {},{}
            L {},{}
            A {},{},{},{},{},{},{}
            L {},{}
            A {},{},{},{},{},{},{}
            z\">""".format(
            color,
            color,
            x1,y1,
            x2,y2,
            maxr,maxr,dth,0,1,x3,y3,
            x4,y4,
            minr,minr,dth,0,0,x1,y1,
            ),file=f)

    # spin from initial angle to final angle (slower at the edge)
    print("""<animateTransform
            attributeName=\"transform\"
            attributeType=\"XML\"
            begin=\"0s\"
            dur=\"{}s\"
            type=\"rotate\" 
            from=\"0 {} {}\"
            to=\"{} {} {}\"
            fill=\"freeze\"
            />""".format(1+r/180,x,y,final_th,x,y),file=f)

    print("</path>",file=f)

def main(depth):
    print("Generating grid")
    grid = klk.gen_grid(klk.gen_stack(depth))
    # klk.disp_grid(grid)

    print("Generating SVG")
    with open("./output/kolakoski{}.svg".format(depth),"w") as f:
        W = 1000
        H = 1000
        R = H/2
        s = R/len(grid)

        # generate svg background
        print("<svg viewBox=\"0 0 ",W," ",H,"\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" >",file=f)
        print("<circle fill=\"white\" cx=\"{}\" cy=\"{}\" r=\"{}\"/>".format(W/2,H/2,R),file=f)

        # generate svg sectors
        dr = s
        for i in range(len(grid)):
            r = i*s + s/2
            dth = 2*pi/(len(grid[i])-1)
            for j in range(len(grid[i])):
                th = 2*pi*j/len(grid[i])
                if grid[i][j] == 1:
                    print_svg_sector(f,W/2,H/2,"black",r,th,dr,dth)

        print("</svg>",file=f)

if __name__ == "__main__":
    depth = 10 
    if len(sys.argv) > 1:
        try:
            depth = int(sys.argv[1])
            assert(depth > 0)
        except:
            print("Depth needs to be a positive integer", file=sys.stderr)
            exit(-1)

    main(depth)

