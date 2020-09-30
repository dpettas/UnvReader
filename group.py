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
        ELEMENT_FLAG = 8
        NODE_FLAG    = 7 

        elem = []

        # loop over the lines 
        for line in self.__lines:

            # split the first lines
            lline = line.split() 

            # The number of the lines should be either 8 or 4
            if len(lline) == NUMCOLS:
               
                # Read the type of the entity 
                tp = int(lline[0])
              

                # If the type is 8 then the entity refers to the id of the
                # surface element

                if tp == ELEMENT_FLAG:  

                    bndelement1 = int(lline[1]) - 1
                    bndelement2 = int(lline[5]) - 1

                    elem.append( bndelement1 )
                    elem.append( bndelement2 )

                elif tp == NODE_FLAG: 
                    raise NotImplementedError("The node case at the group has not implemented yet")



            # there is a case where the number of lines is odd number
            # so the line has only the half columns 
            if len(lline) == int(NUMCOLS/2):

                if tp == ELEMENT_FLAG:  

                    bndelement1 = int(lline[1]) - 1
                    elem.append( bndelement1 )

                elif tp == NODE_FLAG: 
                    raise NotImplementedError("The node case at the group has not implemented yet")



        self.connectivity = elem

    def __iter__(self): return iter(self.__lines)
