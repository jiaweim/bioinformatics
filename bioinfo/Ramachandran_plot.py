import sys

from pyrama import calc_ramachandran, plot_ramachandran

if len(sys.argv) < 2:
    sys.exit("Usage: pyrama my_pdb_file.pdb")

normals, outliers = calc_ramachandran(sys.argv[1:])
plot_ramachandran(normals, outliers)
