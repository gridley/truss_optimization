#!/usr/bin/env python3
# This extracts the figure of merit, sum(|T_i| L_i) from
# each truss. In other words, the sums of magnitudes of tensions
# times lengths of each member.

def obj(infile):
    fom = 0
    with open(infile) as fh:
        for line in fh:
            split_line = line.split()

            # If the line is of this length, it's listing a tension
            if len(split_line) == 5:
                x1 = float(split_line[0])
                y1 = float(split_line[1])
                x2 = float(split_line[2])
                y2 = float(split_line[3])
                tension = abs(float(split_line[4]))
                length = ((x2-x1)**2 + (y2-y1)**2)**.5
                fom += tension * length
    return fom

if __name__ == "__main__":
    import sys
    this_infile = sys.argv[1]
    fom = obj(this_infile)
    print(fom)
