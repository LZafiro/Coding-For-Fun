import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integrate

# The equation of motion of a simple pendulum is
# dth^2/dt^2 = -(G/L)sin(th) => y'' + (G/L)sin(th) = 0
# Let z = y' => z' + (G/L)sin(th) = 0 => z' = -(G/L)sin(th)
# y'(0) = 0
# y(0) = 60 (could change)

# Theta is the angle between the vertical and the pendulum arm
# L is the length of the pendulum arm
# M is the mass of the pendulum bob
# G is the gravity acceleration
L = 1.25  # In meters
M = 1.0  # In kilos
G = 9.81  # m/s^2


# U is named x in this function
# In U: U[0] = y and U[1] = y' = z
def der(x, t):
    # The function returns y', z' = y''
    return [x[1], -(G / L) * np.sin(x[0])]


dt = 0.05
t = np.arange(0, 20, dt)
th = 120  # In degrees
w = 0  # Angular Velocity -> in degrees/s

# Sets the initial states
u = np.radians([th, w])

y = integrate.odeint(der, u, t)

xp = L * np.sin(y[:, 0])
yp = -L * np.cos(y[:, 0])

# -------------------------------------------------------------
# Animation Part

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    line.set_data([0, xp[i]], [0, yp[i]])
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)
plt.show()