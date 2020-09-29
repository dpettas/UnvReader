from   unv.group   import *
from   unv.session import *
import numpy      as np


DELIM = "-1"

def isDelimiter(line: str):
    return line.strip() == DELIM

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Reader 
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

class Reader():
    def __init__(self, filename):
        """
        ** The Reader Class reads a file with a  specific filename.
        ** The file contains:
            filename : the name of the file
            nodes    : the coordinates of the nodes
            surface_elements : the boundary elements of the domain
            elements         : the elements of the domain
        """
        self.filename         = filename
        self.nodes            = np.ndarray(0)
        self.surface_elements = np.ndarray(0)
        self.elements         = np.ndarray(0)


        self.__file     = open(self.filename)
        self.__lines    = self.__file.readlines()

        self.__sessions = []
        self.__groups   = []

        self.__read_structure()
        self.__UNV_id_2411()
        self.__UNV_id_2412()
        self.__UNV_id_2467()


    def getSessionWithId(self, gid: int):

        for session in self.__sessions:
            if session.gid() == gid: return session.lines

        raise ValueError("Wrong argument for gid")

    def getGroupNames(self):
        return [g.title for g in self.__groups]

    def getGroup(self, name) -> Group:

        names = [ g.title for g in self.__groups]

        for g in self.__groups:
            if name == g.title: return g

        raise ValueError("""the name of the group does not exist.
                            Possible values {}""".format(names) )

    def getNumNodes(self):
        return self.nodes.shape[0]

    def getNumElements(self):
        return self.elements.size

    def getNumSurfaceElements(self):
        return self.surface_elements.size


    def getNodeIDsThatBelongToGroup(self,groupname: str):

        out = []
        for elementid in self.getGroup(groupname).connectivity:
            element = self.surface_elements[elementid]
            out.append( element[0] )
            out.append( element[1] )

        out = list( dict.fromkeys(out) )

        return np.asarray( out ) 

    def getNodeCoordinateThatBelongToGroup(self, groupname: str,  direction: str):

        ids = self.getNodeIDsThatBelongToGroup(groupname)

        if   direction.lower() == 'x': dire_ = 0
        elif direction.lower() == 'y': dire_ = 1
        elif direction.lower() == 'z': dire_ = 2
        else: raise ValueError("Wrong Value for direction. Possible: x,y,z")

        out = []
        out = [self.nodes[i][dire_] for i in ids]

        return np.asarray( out )

    def getNodeCoordinates(self, direction: str):

        if   direction.lower() == 'x': dire_ = 0
        elif direction.lower() == 'y': dire_ = 1
        elif direction.lower() == 'z': dire_ = 2
        else: raise ValueError("Wrong Value for direction. Possible: x,y,z")

        out = np.ndarray( self.getNumNodes() )
        for i in range(self.getNumNodes() ):
            out[i] = self.nodes[i][dire_]
        return out

    def getElements(self):
        return self.elements


    def close(self):

        self.__file.close()
        self.filename         = None
        self.nodes            = None
        self.surface_elements = None
        self.elements         = None

        self.__file           = None
        self.__lines          = None

        self.__sessions       = None
        self.__groups         = None

    #<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    # Private Methods  
    #<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    def __read_structure(self):

        opened_session = False
        for i,line in enumerate(self.__lines):

            if   isDelimiter(line) and not opened_session:

                opened_session = True
                init_session   = i + 1

            elif isDelimiter(line) and     opened_session:

                opened_session = False
                final_session  = i - 1

                session_lines = self.__lines[init_session:final_session+1]

                self.__sessions.append( UnvSession(session_lines) )


    def __UNV_id_2411(self):
        """
        """

        node = []
        i = 0
        for line in self.getSessionWithId(2411):
            i +=1
            if not i%2 == 0 and i != 1: node.append( [float(_) for _ in line.split()] )



        self.nodes = np.asarray ( node )

    def __UNV_id_2412(self):

        OneDimensionalElementsFlag = 11

        OneDimensionalElement      = []
        TwoDimensionalElement      = []

        line = self.getSessionWithId(2412)
        # line 0 refers to the gid to the session 
        i = 0
        while True:
            i += 1
            structLine  = [int(_) for _ in line[i].split() ]
            elementType = structLine [1]
            numNodes    = structLine [5]

            if elementType == 11 and numNodes == 2:
                i += 2
                OneDimensionalElement.append( [int(_)-1 for _ in line[i].split()])
            if elementType == 41 and numNodes == 3:
                i += 1
                TwoDimensionalElement.append( [int(_)-1 for _ in line[i].split()])



            if i == len(line)-1: break


        self.surface_elements = np.asarray( OneDimensionalElement )
        self.elements         = np.asarray( TwoDimensionalElement )


    def __UNV_id_2467(self):

        line = self.getSessionWithId(2467)

        # First Element of the the session is the gid of the session
        i = 1
        while True:

            init   = i
            groupLines  = [int(_) for _ in line[i].split()] [-1]
            groupLines  = groupLines + groupLines%2
            groupLines  = int(groupLines/2 )
            i +=  groupLines + 1 # plus one line which is the title
            final = i

            if ( groupLines > 0) :

                self.__groups.append ( Group(  line[init:final+1] ) )




            if i >= len(line) -1: break

