import pynbody
import matplotlib.pylab as plt

#im loading the snapshot

s = pynbody.load('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096')   

#save it by ctrl-x-s 'to save work'



# gonna start loading the halo'galaxies' now

h = s.halos()

#halos we need to only look are # 3,5,6,11,12


pynbody.analysis.angmom.faceon(h[3])

#^^ its centering on the halo that i have picked which is 3 at the moment
#and giving it a shape of a disk almost like a dinner plate

s.physical_units()

#^^ making all the data into a certain amount by mul everything for me

p = pynbody.analysis.profile.Profile(h[3].s,min=.01,max=50)
#^^ starts everything from the center reaching outwards almost like axis


f, axs = plt.subplots(1,2,figsize=(14,6))
#^^ axs helps start making the graph
# its saying to make 2 plots (1,2) so it will make two plots and then giving it #measurments

# make the plot

axs[0].plot(p['rbins'],p['density'],'k')
# rbins means radius , k means black

axs[0].semilogy()
#makes the y axis in a log scale

axs[0].set_xlabel('R [kpc]')
axs[0].set_ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-2}$')
#makes all the nice letters on the side of the axis





