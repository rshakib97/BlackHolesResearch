import pynbody
import matplotlib.pylab as plt
import numpy as np
import glob

files = glob.glob('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.00????/h148.cosmo50PLK.3072g3HbwK1BH.00????')

#print len(files)
for file in files:
	sp = file.split(".")
	s = pynbody.load(file)
#^ loading the snapshot
	iordwewant = 101863883
	BHfilter = pynbody.filt.LowPass('tform',0.0)       # this makes a filter for particles with negative form
	BH = s.stars[BHfilter]                          # this identifies the black holes and makes a black hole object called BH
#want = BH[1]  # BH in halo 3
	Iord = BH['iord']
	#print Iord
	trying = np.where(Iord == iordwewant)
	#print trying
	HaloIds = BH['amiga.grp']
	#print HaloIds
	count = HaloIds[trying]
	#print count
	h = s.halos()
	#haloes we need to only look are #3,5,6,11,12
	pynbody.analysis.angmom.faceon(h[count[0]])
	#^^ centering the halo we have picked
	s.physical_units()
	#^ does the mul for me on the plots
	p = pynbody.analysis.profile.Profile(h[count[0]],min=.01,max=40,ndim=3)
	#^^ addes to the 3-d plot,( this is .g for gass)
	f, axs = plt.subplots(figsize=(14,6))# me changing it to make one plot
	#^ helps start making the graph
	axs.plot(p['rbins'],p['density'], 'k')
	axs.semilogy()
	axs.semilogx()
	axs.set_title('Snapshot '+sp[6])
	axs.set_xlabel("R [kpc]''Density PLOT OF H"+str(count[0]))
	axs.set_ylabel(r'$\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
	#^^^ lines are writing the graph up
	plt.savefig('DensityProfile'+sp[6]+".png")



