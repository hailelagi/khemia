def NewtonSolver(f, xstart, C=0.0):
    """
    Solve f(x) = C by Newton iteration.
    - xstart    starting point for Newton iteration
    - C         constant
    """
    f0 = f(xstart) - C
    x0 = xstart
    dx = 1.0e-6
    n = 0
    while n < 200:
        ff = f(x0 + dx) - C
        dfdx = (ff - f0)/dx
        step = - f0/dfdx

        # avoid taking steps too large
        if abs(step) > 0.1:
            step = 0.1*step/abs(step)

        x0 += step
        emax = 0.00001  # 0.01 mV tolerance
        if abs(f0) < emax and n > 8:
            return x0
        f0 = f(x0) - C
        n += 1
    raise Exception('no root!')
