import pynbody
import matplotlib.pylab as plt


s = pynbody.load('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096')
#^ loading the snapshot



halos = [3,5,6,11,12]


h = s.halos()
s.physical_units()
#haloes we need to only look are #3,5,6,11,12

for count in halos:
	pynbody.analysis.angmom.faceon(h[count])
	p = pynbody.analysis.profile.Profile(h[count],min=.05,max=40,ndim=3,type="log")
	file = open("TableForRadiusG"+str(count)+".txt","w")
	for i in range(len(p['rbins'])):
		row =str(p['rbins'][i])
		file.write(row)
		file.write('\n')
	file.close()
	file = open("TableForDensityG"+str(count)+".txt","w")
	for i in range(len(p['rbins'])):
		row =str(p['density'][i]) 
		file.write(row)
		file.write('\n')
	file.close()

