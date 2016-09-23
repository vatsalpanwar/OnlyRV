from pylab import *
import os
import matplotlib.pyplot as plt
# rc("font", size=14, family="serif", serif="Computer Sans")
# rc("text", usetex=True)

data = loadtxt('HD207832-RV.txt')
#truth = loadtxt('fake_data_like_nuoph.truth')
posterior_sample = atleast_2d(loadtxt('posterior_sample.txt'))

plt.hist(posterior_sample[:,1010], 100)
plt.xlabel('Number of Planets')
plt.ylabel('Number of Posterior Samples')
plt.xlim([-0.5, 10.5])
plt.show()

T = posterior_sample[:,1011:1021]
A = posterior_sample[:,1021:1031]
E = posterior_sample[:,1041:1051]
which = T != 0
T = T[which].flatten()
A = A[which].flatten()
E = E[which].flatten()
# Trim
#s = sort(T)
#left, middle, right = s[0.25*len(s)], s[0.5*len(s)], s[0.75*len(s)]
#iqr = right - left
#s = s[logical_and(s > middle - 5*iqr, s < middle + 5*iqr)]

plt.hist(T/log(10.), 500, alpha=0.5)
plt.xlabel(r'$\log_{10}$(Period/days)')
plt.xlim([0, 5])
#for i in xrange(1009, 1009 + int(truth[1008])):
#  axvline(truth[i]/log(10.), color='r')
plt.ylabel('Number of Posterior Samples')
plt.show()

plt.subplot(2,1,1)
#plot(truth[1009:1009 + int(truth[1008])]/log(10.), log10(truth[1018:1018 + int(truth[1008])]), 'ro', markersize=7)
#hold(True)
plt.plot(T/log(10.), log10(A), 'b.', markersize=1)
plt.xlim([0, 5])
plt.ylim([-1, 3])
plt.ylabel(r'$\log_{10}$[Amplitude (m/s)$]$')

plt.subplot(2,1,2)
#plot(truth[1009:1009 + int(truth[1008])]/log(10.), truth[1038:1038 + int(truth[1008])], 'ro', markersize=7)
#hold(True)
plt.plot(T/log(10.), E, 'b.', markersize=1)
plt.xlabel(r'$\log_{10}$(Period/days)')
plt.ylabel('Eccentricity')
plt.xlim([0, 5])
plt.show()

data[:,0] -= data[:,0].min()
t = linspace(data[:,0].min(), data[:,0].max(), 1000)

saveFrames = False # For making movies
if saveFrames:
    os.system('rm Frames/*.png')


for i in xrange(0, posterior_sample.shape[0]):
    hold(False)
    plt.errorbar(data[:,0], data[:,1], fmt='b.', yerr=data[:,2])
    hold(True)
    plt.plot(t, posterior_sample[i, 0:1000], 'r')
    plt.xlim([-0.05*data[:,0].max(), 1.05*data[:,0].max()])
    plt.ylim([-1.5*max(abs(data[:,1])), 1.5*max(abs(data[:,1]))])
    #axhline(0., color='k')
    plt.xlabel('Time (days)', fontsize=16)
    plt.ylabel('Radial Velocity (m/s)', fontsize=16)
    plt.draw()
    print 1
#     if saveFrames:
#         plt.savefig('Frames/' + '%0.4d'%(i+1) + '.png', bbox_inches='tight')
    #print('Frames/' + '%0.4d'%(i+1) + '.png')



plt.show()
