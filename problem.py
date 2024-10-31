import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def swimmer_ode(x, y, vs, vr):
    return (vs * y - vr * np.sqrt(x**2 + y**2))/(vs * x)


vs = 2
vr = 1


y0 = [0]  


solution = solve_ivp(swimmer_ode, [1, 0], y0, args=(vs, vr), dense_output=True)


x_vals = np.linspace(1, 0, 1000)
y_vals = solution.sol(x_vals)

# Plot the solution
plt.figure(figsize=(10, 8))
plt.plot(x_vals, y_vals[0], 'b-', label=f'vs={vs}, vr={vr}')
plt.grid(True)
plt.xlabel('Distance from West Shore (miles)')
plt.ylabel('Distance Northward (miles)')
plt.title("Swimmer's Path Across River with Initial Condition y(1)=0")
plt.legend()
plt.axis('equal')
plt.show()

# Print final position
print("Final position (x,y) = ("+str(x_vals[-1])+", "+str(y_vals[0][-1])+")")