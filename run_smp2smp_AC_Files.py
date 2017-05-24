
import os


RUNS = range(1,51)
#a=range(39,51)
#b=range(96,101)
#c=range(145,151)
#d=range(177,201)
#e=range(241,251)
#f=range(292,301)
#g=[30,81,131,276]
#list_removed = a#+b+c+d+e+f+g
#
#for item in list_removed:
#    RUNS.remove(item)
#print RUNS

for i in RUNS: 
    os.system('del smp2smp_in_ins.txt')
    f = open('smp2smp_in_tpl.txt', 'r')    
    lines=f.readlines()
    f.close()  
    f = open('smp2smp_in_ins.txt', 'w')   
    for line in lines:  
        line=line.strip('\n')
        if line[0] == 'A':
            line=line.split('#')
            print >> f, str(line[0])+ str(i) + str(line[1])
        else:
            print >> f, str(line)
    f.close()
    os.system('smp2smp<smp2smp_in_ins.txt')