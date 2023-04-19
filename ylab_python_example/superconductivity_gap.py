from math import log, exp, pi, tanh, sqrt
from scipy import integrate, optimize
from numpy import euler_gamma
import matplotlib.pyplot as plt


q = log(10 * 4 * exp(euler_gamma) / pi)


def gap(t):
    if t >= 1:
        return 0
    if t < 0.001:
        t = 0.001

    def gap_integral(d):
        def gap_integrand(x):
            return tanh(sqrt(x**2 + d**2) / t) / sqrt(x**2 + d**2)

        return integrate.quad(gap_integrand, 0, 10)[0] - q

    return optimize.bisect(gap_integral, 0.001, 2)


if __name__ == "__main__":
    t = [x * 0.01 + 0.01 for x in range(0, 110)]
    d = [gap(x) for x in t]

    fig = plt.figure(figsize=(6, 4), dpi=150)
    fig.subplots_adjust(left=0.15, right=0.95, bottom=0.15, top=0.9)
    ax = fig.add_subplot(111)

    ax.plot(t, d, "-")
    ax.set_xlabel("$t=T/T_C$")
    ax.set_ylabel("$\Delta(t)/\Delta(0)$")
    ax.tick_params(which="major", direction="in")
    ax.tick_params(which="minor", direction="in")
    ax.minorticks_on()

    plt.savefig("gap.png")
