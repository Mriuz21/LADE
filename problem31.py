from sympy import symbols, integrate, solve, Eq

x = symbols('x')

v_s_value = 2
v_r_function = 30 * x * (1 - x)

integrated_y = integrate(-v_r_function / v_s_value, x)

C = symbols('C')
y_solution = integrated_y + C
C_value = solve(Eq(y_solution.subs(x, 1), 0), C)[0]

final_y_solution = y_solution.subs(C, C_value)
print(final_y_solution)