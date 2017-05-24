from Monte_carlo_utilities import *
from numpy import mean, std, array, amin, amax
from pylab import savefig, subplots_adjust


################### main program

d_file_cal='Calibrated_Solution\\GetTransientHeadObsSMP_AC_CalSol.smp' #drawdown
#
#create list of indices of files produced in MC analysis
filelist=range(1,301) #201
#removelist=[20,30,35,36,43]
#for i in removelist: 
#    filelist.remove(i)
#print filelist
dbase_file='Step3_AC_Results\\AC_GetTransientHeadObsSMPparam'  #basename of drawdown files

dd=smp2dict(d_file_cal)
max_dd_change=max_SMP(dd)

MC_drawdown_max=max_SMP_list(dbase_file,filelist,1,1,'.smp')


print MC_drawdown_max.keys()

#close('all')
#im=matplotlib.image.imread('Matrix_logo2.png')
pp = PdfPages('Montecarlo_Iteration_Figures.pdf')
fignum=24


obsDict = {'1_9219_3':'OBS1 Grosmont','4_9019_3':'OBS2 Grosmont','5_9020_3':'OBS3 Grosmont','11_8720_3':'OBS4 Grosmont', \
                '1_9219_6':'OBS1 Leduc - Cooking Lake','4_9019_6':'OBS2 Leduc - Cooking Lake','5_9020_6':'OBS3 Leduc - Cooking Lake','11_8720_6':'OBS4 Leduc - Cooking Lake'}
obsDict_sorted = sorted(obsDict, key=obsDict.get, reverse=False)
for key in obsDict_sorted:
    min = []
    max = []
    means = []
    std_dev = []
    for i in range(len(filelist)):
        if i > 2:
            #print MC_drawdown_max[key]['value_of_max_change'][i]
            values = array(MC_drawdown_max[key]['value_of_max_change'][:i])
            ave = mean(values)
            means.append(ave)
            standard_deviation = std(values)
            std_dev.append(standard_deviation)
            minimum = amin(values)
            min.append(minimum)
            maximum = amax(values)
            max.append(maximum)
    iter = array(range(3,len(std_dev)+3))
    fig1=figure(fignum, figsize=(11,8.5), dpi=None, facecolor=None, frameon=True)
    subplots_adjust(wspace=0.3, hspace=0.125, left=0.15, right=0.9, bottom=0.2,top=0.8)
    #figimage(im,375,40)
    #fig1.suptitle('FIGURE A-'+str(fignum)+': Observation Point - '+str(obsDict[key]), fontsize=8)
    fig1.text(0.925,0.8631, 'Figure 6B-'+str(fignum)+'\nMonte Carlo Simulations Predictions Statistics vs. Iterations, '+str(obsDict[key]), horizontalalignment='right', fontsize=9, color='white', bbox={'edgecolor':(0.0902,0.3922,0.5569),'facecolor':(0.0902,0.3922,0.5569), 'alpha':1.0, 'pad':15})
    fig1.text(0.04631,0.8631,'Koch Oil Sands Operating ULC\nDunkirk In Situ Project', horizontalalignment='left', fontsize=9, color='white', bbox={'edgecolor':(0.0902,0.3922,0.5569),'facecolor':(0.0902,0.3922,0.5569), 'alpha':1.0, 'pad':15})
    fig1.text(0.47,0.15, 'Number of iterations', fontsize=7)
    bx1=subplot(311)
    scatter(iter, std_dev, s=10)
    grid(c='k')
    tick_params(axis='both', labelsize='xx-small')
    bx1.set_ylabel('Standard Deviation (m)\n\n', fontsize=7, horizontalalignment='center') #'x-small'
    bx1.set_xlim(0,300)
    bx2=subplot(312)
    scatter(iter, means, s=10)
    grid(c='k')
    tick_params(axis='both', labelsize='xx-small')
    bx2.set_ylabel('Mean (m)\n\n', fontsize=7, horizontalalignment='center')
    bx2.set_xlim(0,300)
    bx3=subplot(313)
    scatter(iter, min, s=10)
    scatter(iter, max, s=10)
    grid(c='k')
    tick_params(axis='both', labelsize='xx-small')
    bx3.set_ylabel('Minimum/Maximum\nValues (m)\n\n', fontsize=7, horizontalalignment='center')
    bx3.set_xlim(0,300)
    savefig(pp, facecolor='none', orientation=['landscape'], format='pdf', papertype='letter')
    #print means
    #print std_dev
    fignum=fignum+1
pp.close()
