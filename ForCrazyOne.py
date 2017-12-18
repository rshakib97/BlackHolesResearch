import pynbody
import matplotlib.pylab as plt



s = pynbody.load('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.002688/h148.cosmo50PLK.3072g3HbwK1BH.002688')
#^ loading the snapshot

h = s.halos()
#haloes we need to only look are #3,5,6,11,12

pynbody.analysis.angmom.faceon(h[10])
#^^ centering the halo we have picked

s.physical_units()
#^ does the mul for me on the plots

p = pynbody.analysis.profile.Profile(h[10],min=.01,max=40,ndim=3)
#^^ addes to the 3-d plot,( this is .g for gass)

f, axs = plt.subplots(figsize=(14,6))# me changing it to make one plot
#^ helps start making the graph

axs.plot(p['rbins'],p['density'], 'k')
axs.semilogy()
axs.set_xlabel('R [kpc]''Density PLOT OF H10')
axs.set_ylabel(r'$\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
#^^^ lines are writing the graph up
plt.savefig("ThePlotFor11.png")
