import numpy as np


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Group Class
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

class Group():

    def __init__(self, lines: str):
        
        self.title = lines[1].strip().replace(" ","_").replace("\n","")
       
        struct = [int(_) for _ in lines[0].split() ]

        self.numBnd   = struct[0] 
        self.numLines = struct[-1] + struct[-1]%2
        self.numLines = int(self.numLines/2)
        # Return the id of the surface element that belongs to that group 
        self.connectivity = list() 


        self.__lines = lines
        self.__connectivity()

    def __connectivity(self): 
        """
        reads the connectivity from the corresponding boundary
        """
        NUMCOLS      = 8 

        elem = []

        # loop over the lines 
        for line in self.__lines:

            # split the first lines
            lline = line.split() 

            # The number of the lines should be either 8 or 4
            if len(lline) == NUMCOLS:
               
            
                # If the type is 8 then the entity refers to the id of the
                # surface element
                if self.__isElementGroup(line):  
                    bndelement1 = int(lline[1]) - 1
                    bndelement2 = int(lline[5]) - 1

                    elem.append( bndelement1 )
                    elem.append( bndelement2 )

                elif self.__isNodeGroup(line): 
                    raise NotImplementedError("The node case at the group has not implemented yet")



            # there is a case where the number of lines is odd number
            # so the line has only the half columns 
            if len(lline) == int(NUMCOLS/2):

                if self.__isElementGroup(line):  

                    bndelement1 = int(lline[1]) - 1
                    elem.append( bndelement1 )

                elif self.__isNodeGroup(line): 
                    raise NotImplementedError("The node case at the group has not implemented yet")



        self.connectivity = elem

    def __isElementGroup(self,line: str):
        
        # This is a list of integers 
        ELEMENT_FLAG = 8
        flags        = [ int(itm) for itm in line.split() ]
        if flags[0] == ELEMENT_FLAG and flags[-1] == 0:
            return True
        return False

    def __isNodeGroup(self,line: str):
        
        # This is a list of integers 
        NODE_FLAG    = 7
        flags        = [ int(itm) for itm in line.split() ]
        if flags[0] == NODE_FLAG and flags[-1] == 0:
            return True
        return False

    def __iter__(self): return iter(self.__lines)
