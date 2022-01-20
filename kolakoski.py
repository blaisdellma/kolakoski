#!/usr/bin/env python

# Generates the Kolakoski sequence up to a specific depth (iteration)
#   as well as a grid for display of the produced pattern (see Numberphile video)
#
# https://www.youtube.com/watch?v=co5sOgZ3XcM
# https://en.wikipedia.org/wiki/Kolakoski_sequence)

import sys

# get next Kolakoski sequence from previous sequence
def next_seq(seq):
    nseq = []
    ch = 2
    for j in range(len(seq)):
        for k in range(seq[j]):
            nseq.append(ch)
        ch = 3-ch
    return nseq

# generate Kolakoski sequence at a specified depth
def gen_seq(depth):
    seq = [2]
    for i in range(depth):
        seq = next_seq(seq)

    return seq

# print out the sequence
def print_seq(seq):
    print(", ".join([str(x) for x in seq]))

# generate Kolakoski sequences up to a specified depth
def gen_stack(depth):
    stack = [[2]]
    for i in range(depth):
       seq = stack[len(stack)-1]
       stack.append(next_seq(seq))

    return stack

# print out all sequences in list
def print_stack(stack):
    for i in range(len(stack)):
        print_seq(stack[i])

# convert list of sequences in grid for display
# by repeating elements in the earlier shorter
# sequences to match with the elements of the 
# later elements they generate
def gen_grid(stack):
    cnts = [[(x,1) for x in y] for y in stack]
    for i in range(len(stack)-2,-1,-1):
        ind = 0
        for j in range(len(stack[i])):
            val = 0
            for k in range(stack[i][j]):
                val += cnts[i+1][ind][1]
                ind += 1
            cnts[i][j] = (stack[i][j],val)

    grid = []
    for i in range(len(cnts)):
        grid.append([])
        for j in range(len(cnts[i])):
            for k in range(cnts[i][j][1]):
                grid[i].append(cnts[i][j][0])

    return grid

# print out the grid as 1's and 2's
def print_grid(grid):
    for i in range(len(grid)):
        print_seq(grid[i]);

# print out the grid as two seperate characters
def disp_grid(grid,ch1=' ',ch2='%'):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(ch2 if grid[i][j] == 2 else ch1,end='')
        print("");

# take arg1 as depth
if __name__ == '__main__':
    print("KOLAKOSKI SEQUENCE GENERATOR")
    depth = 4
    if len(sys.argv) > 1:
        try:
            depth = int(sys.argv[1])
        except:
            print("Please give an integer depth",file=sys.stderr)
            sys.exit(-1)

    # print_seq(gen_seq(depth))
    # print_stack(gen_stack(depth))
    # print_grid(gen_grid(gen_stack(depth)))
    disp_grid(gen_grid(gen_stack(depth)),'.')
