import smp_name_correction as smpcor



base_file = 'AC_GetTransientHeadObsSMPparam'
ext = '.out'

RUNS = range(1,51)
#a=range(39,51)
#b=range(96,101)
#c=range(145,151)
#d=range(177,201)
#e=range(241,251)
#f=range(292,301)
#g=[30,81,131,276]
#list_removed = a#+b+c+d+e+f+g

#for item in list_removed:
#    RUNS.remove(item)
#print RUNS

for i in RUNS:
    file = base_file + str(i) + ext
    print file
    instance = smpcor.name(file,'th','')
    instance.run()