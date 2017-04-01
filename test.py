def fx_calc(x_values,coefficients):
    def f(x):
        fx = 0
        for ind,i in enumerate(coefficients):
            print(ind,i,x)
            fx+=i*(x**ind)
            print(fx)
        return fx

    fx_values = []
    for x in x_values:
        fx = f(x)
        fx_values.append(fx)
    return fx_values


print(fx_calc([0],[4]))