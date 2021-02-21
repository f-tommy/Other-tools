#!/usr/bin/env python3                                                          
# interpolate_2d.py input1 input2 N
# INPUT1: 2-colmns data (1:time, 2:data)
# INPUT2: 1-colmns data (1:time) for output time series
# N: interpolation method
#     1: 1d-linear interpolation
#     2: 2d-spline interpolation
#     3: 3d-spline interpolation
#     4: Nearest interpolation
#     5: 3d-Hermite interpolation
#     6: Akima interpolation
#     7: Barycentric interpolation
#     8: Krough interpolation
#     9: Lagrange interpolation
import sys
import numpy as np
from scipy import signal,interpolate

# Obtain argument
args = sys.argv

# Read data
data1 = np.loadtxt(args[1])
data2 = np.loadtxt(args[2])
t0 = data1[:,0]
x0 = data1[:,1]
t1 = data2
n = int(args[3])
                                                                               
# Interpolation
if n == 1:
    # linear-interpolate
    sys.stderr.write('N = 1: Linear-interpolation\n')
    f = interpolate.interp1d(t0,x0)
    x1 = f(t1)
elif n == 2:
    # 2d-spline interpolate
    sys.stderr.write('N = 2: 2d Spline-interpolation\n')
    f = interpolate.interp1d(t0,x0,kind="quadratic")
    x1 = f(t1)
elif n == 3:
    # 3d-spline interpolate
    sys.stderr.write('N = 3: 3d Spline-interpolation\n')
    f = interpolate.interp1d(t0,x0,kind="cubic")
    x1 = f(t1)
elif n == 4:
    # Nearest interpolate
    sys.stderr.write('N = 4: Nearest-interpolation\n')
    f = interpolate.interp1d(t0,x0,kind="nearest")
    x1 = f(t1)
elif n == 5:
    # 3d Hermite interpolate
    sys.stderr.write('N = 5: 3d Hermite-interpolation\n')
    f = interpolate.PchipInterpolator(t0,x0)
    x1 = f(t1)
elif n == 6:
    # Akima interpolate
    sys.stderr.write('N = 6: Akima-interpolation\n')
    f = interpolate.Akima1DInterpolator(t0,x0)
    x1 = f(t1)
elif n == 7:
    # Barycentric interpolate
    sys.stderr.write('N = 7: Barycentric-interpolation\n')
    f = interpolate.BarycentricInterpolator(t0,x0)
    x1 = f(t1)
elif n == 8:
    # Krogh interpolate
    sys.stderr.write('N = 8: Krogh-interpolation\n')
    f = interpolate.KroghInterpolator(t0,x0)
    x1 = f(t1)
elif n == 9:
    # lagrange interpolate
    sys.stderr.write('N = 9: Lagrange-interpolation\n')
    f = interpolate.lagrange(t0,x0)
    x1 = f(t1)
else:
    sys.stderr.write('! Argument N is not defined\n')
    sys.exit()

# Output
out = np.vstack((t1,x1))
np.savetxt(sys.stdout, out.T)
