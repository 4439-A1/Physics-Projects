'''
Visit: https://trinket.io/glowscript/22e93f31c2
'''
GlowScript 2.9 VPython

# Solves the linear-drag falling object problem using an Euler integrator

# Create some windows in which to graph our results
poswindow = gdisplay(xtitle="Time", ytitle="Position") 
velwindow = gdisplay(xtitle="Time", ytitle="Velocity") 

# We will graph two different position curves (solved with different timesteps, 
# different integrators, or whatever)
yplot1 = series(color=color.black,gdisplay=poswindow)
yplot2 = series(color=color.red,gdisplay=poswindow)
yplot3 = series(color=color.green,gdisplay=poswindow)

# ... and the same with velocity
vplot1 = series(color=color.black,gdisplay=velwindow)
vplot2 = series(color=color.red,gdisplay=velwindow)
vplot3 = series(color=color.green,gdisplay=velwindow)


# Input parameters for model
dt = 0.05 # time step (s)
theta = 45 # launch angle (degrees)
vi_x = 40 * cos(theta * 3.141 / 180) # initial x velocity (m/s)
vi_y = 40 * sin(theta * 3.141 / 180) # initial y velocity (m/s)
xi = 0 # initial x position (m)
yi = 0  # initial y position (m)
m = 0.0027  # mass of sphere (kg)
g = 10  # gravity (m/s^2)
D = 0.5 # drag coefficient
rho = 1.25 # air density (kg/m^2)
r = 0.002 # radius
A = 3.141 * (r ** 2) # cross-sectional area (m^2)
tmax = 50 # how long should we run the simulation? (s)
FR = 20/dt  #animaion rate.


vx = vi_x # set the actual variables we will use, v and y, to their initial values
vy = vi_y
x=xi
y=yi
t=0


# Use Modified Euler's method to approximate

while t < tmax+dt:
    rate(FR)
    yplot2.plot(t,y)
    vplot2.plot(t,vy)
    yplot3.plot(t,x)
    vplot3.plot(t,vx)
    if y<0:
      tmax = t + dt
      break
    vtemp = vx
    vx= vx - (rho * D * A / 2 / m * vx**2)*dt
    x= x + 0.5*(vx + vtemp)*dt
    vtemp = vy
    if(vy >= 0):
      vy= vy - (g + rho * D * A / 2 / m * vy**2)*dt
    else:
      vy= vy + (-g + rho * D * A / 2 / m * vy**2)*dt
    y= y + 0.5*(vy + vtemp)*dt
    t += dt

print ('vf_y = ',vy,'  yf = ',y)
print ('vf_x = ',vx,'  xf = ',x)
