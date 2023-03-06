#wave equation by forward Euler method 1D simple
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 2.0  # length of the string
c = 1.0  # wave speed
T = 10.0  # total simulation time
dt = 0.01  # time step
dx = 0.1  # space step
nx = int(L/dx) + 1  # number of grid points
nt = int(T/dt)  # number of time steps

# Initialize the displacement array
u = np.zeros((nx, nt))

# Set the initial conditions
for i in range(nx):
    x = i * dx
    u[i, 0] = np.sin(0.5*np.pi * x)+0.5*np.sin(np.pi * x)+0.2*np.sin(2*np.pi * x)+0.1*np.sin(4*np.pi * x)

# Time stepping loop
for n in range(nt-1):
    for i in range(1, nx-1):
        u[i, n+1] = 2*(1-c**2*dt**2/dx**2)*u[i, n] - u[i, n-1] + c**2*dt**2/dx**2*(u[i+1, n]+u[i-1, n])
    u[0, n+1] = 0
    u[-1, n+1] = 0

# Plotting and animation
x = np.linspace(0, L, nx)

fig, ax = plt.subplots()
line, = ax.plot(x, u[:, 0])

def animate(n):
    line.set_ydata(u[:, n])  # update the data
    return line,

ani = animation.FuncAnimation(fig, animate, range(nt), interval=10, blit=True)
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.ylim([-100,100])
plt.show()
ani.save('oscillation.mp4', writer='ffmpeg', fps=60, dpi=300)
