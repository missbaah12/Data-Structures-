#index number 6931521
#this scipt belongs to Gloria Ofosua Baah
#this code is for calculating bending moment and shear force
import numpy as np

L = 12 #length of beam in meters
w = 10 #intensity of load in KN/m

#Bending moment at x=0
x = 0
M0 = (w*(-6*x**2 + 6*L*x-L**2))/12
print(M0) # the bending moment value at x = 0

#shear force at x=0
x=0
V0 = w*(L/2 - x)
print(V0) # shear force value at 0

#bending moment at x=L
x = L
Ml= (w*(-6*x**2 + 6*L*x-L**2))/12
print(Ml)

#shear force at x=L
Vl = w*(L/2 - x)
print(Vl)

#distances at which bending moment will be zero
#the two roots are;
a = 1
b = -L
c = L**2/6
x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
x2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
print(x1)
print(x2)

#distance at which shear force is 0
x3 = L/2
print(x3)

x4 = np.arange(0,12.01,0.01) 
Mdis= (w*(-6*x4**2 + 6*L*x4-L**2))/12
print(Mdis)

Vdis = w*(L/2 - x4)
print(Vdis)

m_Mdis = np.min(np.abs(Mdis))
a1 = 1
b1 = -L
c1 = (L**2/6)+(2*m_Mdis)/w
#Using the Almighty formula the two roots are;
x5 = (-b1 + np.sqrt(b1**2 - 4*a1*c1))/2*a1
x6 = (-b1 - np.sqrt(b1**2 - 4*a1*c1))/2*a1
print(x5)
print(x6)

#Question g

relerror_1 = ((x1 - x2)/x1*100) 
relerror_2 = ((x5 - x6)/x6*100)
print(relerror_1)
print(relerror_2)

#maximum and minimum point
#maximum
max_M = np.max(M0)
a3 = 1
b3 = -L
c3 = (L**2/6)+(2*max_M)/w
#Using the Almighty formula the two roots are;
x7= (-b3 + np.sqrt( b3**2 - 4*a3*c3))/2*a3
x8 =(-b3 - np.sqrt( b3**2 - 4*a3*c3))/2*a3
print(x7)
print(x8)

#for the minimum
min_M = np.min(M0)
a4 = 1
b4 = -L
c4 = (L**2//6)+(2*min_M)/w
#Using the Almighty formula the two roots are;
x9 = (-b4 - np.sqrt(b4**2 - 4*a4*c4))/2*a4
x10 = (-b4 + np.sqrt(b4**2 - 4*a4*c4))/2*a4
print(x9)
print(x10)


#github repository https://github.com/misbaah12




