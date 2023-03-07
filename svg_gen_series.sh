#!/usr/bin/env bash

# generate svg for multiple depths
for ((x=8; x<=15; x++)); do
	./gen_svg.py $x 0 > /dev/null;
	./gen_svg.py $x 1 > /dev/null;
done
