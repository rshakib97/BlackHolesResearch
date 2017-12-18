import pynbody
import matplotlib.pylab as plt


s = pynbody.load('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096')
#^ loading the snapshot


h = s.halos()
#haloes we need to only look are #3,5,6,11,12

G=[3,5,6,11,12]

for count in G:

    pynbody.analysis.angmom.faceon(h[count])
    #^^ centering the halo we have picked

    s.physical_units()
    #^ does the mul for me on the plots

    p = pynbody.analysis.profile.Profile(h[count],min=.01,max=60,ndim=3)
    #^^ addes to the 3-d plot,( this is .g for gass)

    f, axs = plt.subplots(1,1,figsize=(8,6))# me changing it to make one plot
    #^ helps start making the graph



    axs.plot(p['rbins'],p['density'], 'k')
    axs.semilogy()
    axs.set_xlabel('R[kpc]''Total Density Plot OF H'+str(count),fontsize = 20)
    axs.set_ylabel(r'$\rho_{ϱ}$ [M$_{\odot}$ kpc$^{-3}$]', fontsize = 20)
    #^^^ lines are writing the graph up

    plt.savefig("ThePlots"+str(count)+".png")


#^ will plot and show it
#plt.savefig("ThePlots.png")

	
