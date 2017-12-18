import numpy as np
import matplotlib.pylab as plt
import math
from scipy.optimize import curve_fit

def func1(r,rhoc,rs):
	return (rhoc)/( r/rs * ( 1+r/rs)**2)


def func2(r,rhoo,ro):
	return rhoo* ( ro**3)/((r+ro)*(r**2+ro**2))



f = [3,5,6,11,12]

fi = open("TableForCurveFitData.txt","w")

for count in f:

	file = open("TableForDensityG"+str(count)+".txt","r")
	file2 = open("TableForRadiusG"+str(count)+".txt","r") 


	y = []
	for row in file:
		y.append(float(row))

#print y

	x = []
	for row in file2:
		x.append(float(row))

	#print x

	x = np.array(x)
	y = np.array(y)


# density is Y!!!

	rhoc = 1e6
	rs = 4.0

	rhoo = 1e6
	ro = 4.0



	if(count == 11):
		rhoc = 1e2
		rs = 20.0
		rhoo = 1e2
		ro = 20.0
		
	popt, pcov = curve_fit(func1, x, y,p0=[rhoc,rs],maxfev = 10000)
	plt.plot(x, func1(x, *popt), 'r-', label='Cusp')

#	print popt

	popt, pcov = curve_fit(func2, x, y,p0=[rhoo,ro])
	plt.plot(x, func2(x, *popt), 'g--', label='Core')

#	print "DataForGalaxyCurve "+str(count),popt
	wri= str(popt)
	fi.write("DataForGalaxyCurve "+str(count)+ " ")
	fi.write(wri)
	fi.write('\n')
	plt.title(str(count))
	plt.plot(x,y, 'b', label='Data')
	plt.xlabel('Radius',fontsize=20)
	plt.ylabel('Density',fontsize=20)
	plt.legend()
	plt.xscale("log")
	plt.yscale("log")
	plt.savefig("CurvePlotForGalaxy"+str(count)+".png")
	#plt.savefig("CurvePlotForGalaxy"+str(count)+".png")
	#plt.show()

	file.close()
	file2.close()
	

fi.close()



