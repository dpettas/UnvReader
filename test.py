import matplotlib.pyplot as plt
import unv
import timeit 


# Read the unv file
unvfile = unv.Reader("./Mesh_2.unv")



# Get the coordinates of the bulk nodes 
xt = unvfile.getNodeCoordinates('x')
yt = unvfile.getNodeCoordinates('y')

# Get the bulk elements
triangles = unvfile.getElements()


# Boundary elements 
# Read Groups and plot the boundary nodes 

color = "#000000"
x = unvfile.getNodeCoordinateThatBelongToGroup('Inflow','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('Inflow','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

x = unvfile.getNodeCoordinateThatBelongToGroup('wall','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('wall','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

x = unvfile.getNodeCoordinateThatBelongToGroup('Outflow','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('Outflow','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

x = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry1','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry1','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

x = unvfile.getNodeCoordinateThatBelongToGroup('Bubble','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('Bubble','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)

x = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry2','x')
y = unvfile.getNodeCoordinateThatBelongToGroup('Symmetry2','y')
for i in range(x.size): plt.scatter(x,y,color = color, s = 10)



plt.axis('off')
plt.triplot(xt, yt, triangles, linewidth = 0.5)
plt.axes().set_aspect(1.0)
plt.tight_layout()

plt.show()



















