import numpy as np;

class linear:
    dx = 0.01;

    def __init__(self, funcs):
        self.funcs = funcs;

    def run(self, inits, xf):
        x_vals = np.arange(0, xf, self.dx);
        y_vals = [];
        y_vals.append(inits[-1]);

        inits.insert(0, 0);

        for x in x_vals:
            if (x == 0):
                continue;

            ypm = 0;
            for i in np.arange(len(inits) - 1):
                ypm += (inits[i + 1] * self.funcs[i + 1](x));

            inits[0] = ((self.funcs[-1](x) - ypm) / self.funcs[0](x));

            for i in np.arange(len(inits) - 1):
                inits[i + 1] += (self.dx * inits[i])

            y_vals.append(inits[-1]);


        return[x_vals, y_vals];
