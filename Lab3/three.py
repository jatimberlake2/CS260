from grid import Grid
from arrays import Array
from node import Node

def main():
	cube = Grid(3,3)
	array = []
	for i in range(cube.getHeight()):
		for j in range(cube.getWidth()):
			cube[i][j] = Array(3)
	for x in range(cube.getHeight()):
		for y in range(cube.getWidth()):
			for z in range(len(cube[x][y])):
				cube[x][y][z] = str(x)+str(y)+str(z)
				array.append(cube[x][y][z])
#	print(array)
	head = None
	for count in range(len(array)-1,-1,-1):
		head = Node(array[count], head)
	while head != None:
		print(head.data)
		head = head.next

main()
