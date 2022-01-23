#!/usr/bin/env bash

# generate svg for multiple depths
for ((x=8; x<=15; x++)); do
	./gen_svg.py $x > /dev/null;
done
