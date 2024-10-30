import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the differential equation
def swimmer_ode(x, y, vs, vr):
    return (vs * y - vr * np.sqrt(x**2 + y**2))/(vs * x)

# Parameters
vs = 1  # swimmer's speed
vr = 2  # river's speed

# Initial condition
y0 = [0]  # y(1) = 0

# Solve the ODE
solution = solve_ivp(swimmer_ode, [1, 0], y0, args=(vs, vr), dense_output=True)

# Generate x values for plotting
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