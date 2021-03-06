import matplotlib.pyplot as pl2
import unv
import timeit 


# refinement = unv.Reader("./Mesh_2.unv")
refinement = unv.Reader("/home/pettas/coalescence.unv")
refinement.toAsciiTecplot("test.plt",zone="coal",renameCoords="Z R")
# refinement.exportTofolder("test", zero_based = False)


# orig = unv.Reader("/home/pettas/MyWork/LabFem/tecplot/time_204.0000.plt")
# orig.exportTofolder("test", zero_based = False)


# # Get the coordinates of the bulk nodes 
# xt        = refinement.getNodeCoordinates('x')
# yt        = refinement.getNodeCoordinates('y')
# triangles = refinement.getElements()

# # refinement.toAsciiTecplot("test.plt","refined1",renameCoords = "Z R")
# plt.triplot(xt, yt, triangles, linewidth = 1.5)


# xt        = orig.getNodeCoordinates('x')
# yt        = orig.getNodeCoordinates('y')
# triangles = orig.getElements()
# plt.triplot(xt, yt, triangles, linewidth = 1.0)


# plt.axes().set_aspect(1.0)
# plt.show()

# plt.axis('off')
# plt.axes().set_aspect(1.0)
# plt.tight_layout()

# plt.show()

# Get the bulk elements


# Boundary elements 
# Read Groups and plot the boundary nodes 

#color = "#000000"
#x = unvfile.getNodeCoordinateThatBelongToGroup('Inflow','x')
#y = unvfile.getNodeCoordinateThatBelongToGroup('Inflow','y')
#for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

# x = unvfile.getNodeCoordinateThatBelongToGroup('Wall','x')
# y = unvfile.getNodeCoordinateThatBelongToGroup('Wall','y')
# for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

# x = unvfile.getNodeCoordinateThatBelongToGroup('Outflow','x')
# y = unvfile.getNodeCoordinateThatBelongToGroup('Outflow','y')
# for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

#x = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry1','x')
#y = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry1','y')
#for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

# x = unvfile.getNodeCoordinateThatBelongToGroup('Bubble','x')
# y = unvfile.getNodeCoordinateThatBelongToGroup('Bubble','y')
# for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

#x = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry2','x')
#y = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry2','y')
#for i in range(x.size): plt.scatter(x,y,color = color, s = 10)





















