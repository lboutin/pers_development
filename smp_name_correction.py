
class name:
    """Class that changes obsnames in a smp format file. 
    """
    
    def __init__(self, _filein, _charCHG, _charREP):
        """Instanciation method.
        """
        self.file = _filein
        self.charCHG = _charCHG
        self.charREP = _charREP
        
    def run(self):
        #fin = 'AC_GetTransientHeadObsSMPparam1.out'
        f = open(self.file,'r')
        #fout = 'AC_GetTransientHeadObsSMPparam1_cor.out'
        _fout = str(self.file)+".cor"
        f2 = open(_fout,'w')
        
        lines = f.readlines()
        for line in lines:
            line=line.replace(self.charCHG, self.charREP)
            f2.write(line)
        f.close()
        f2.close()