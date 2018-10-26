# python-3 values example
import math

# python integers are unbounded

print ("Python-3 long integer examples")

distance_to_Andromeda_galaxy_ly = 2537000 #light years
light_speed = 299792458 # m/s
distance_to_Andromeda_galaxy_m = distance_to_Andromeda_galaxy_ly * light_speed
print("Distance to Andromeda galaxy(m) = ", distance_to_Andromeda_galaxy_m)

print("google (10*100) = ", 10**100)

print ("\nPython-3 float examples")

f1 = math.pi
print("f1 = ", f1)
f2 = 2.1e-56
print("f2 = ", f2)
print("Ops! do not comare floats to equivalence: '.1 + .1 + .1 == .3' is False!\n", .1 + .1 + .1 == .3) 

print ("\nPython-3 complex examples")

x = complex(1, 2)
print("x = ", x)
print("x.real = ", x.real)
print("x.imag = ", x.imag)

