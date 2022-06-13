import ODE;
import numpy as np;
import math;
import matplotlib.pyplot as plt;

def c1(x):
    return 1;

def c2(x):
    return 1;

def c3(x):
    return 1;

def f(x):
    return 1;

eq_1 = ODE.linear([c1, c2, c3, f]);
eq_1.dx = 0.001
sols = eq_1.run([1, 1], 10);

plt.plot(sols[0], sols[1]);
plt.grid();
plt.show();
