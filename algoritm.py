def recursive(x, y, m, visited,length, dir):
	# print("\nx: " + str(x))
	# print("y: " + str(y))
	# print("dir: " + str(dir))
	# print("length: " + str(length))
	if canBePlaced(x,y,m,dir):

		visited.append([x,y,dir])
		a = recursive(x + 3*dir, y, m, visited, length + 1, dir)[0]
		b = recursive(x + 2*dir, y + 1, m, visited, length + 1, -1*dir)[0]
		return [max(a, b), visited]
	else:
		# print "fail"
		return [length, visited]

def canBePlaced(x,y,m,dir):
	if dir == 1:
		if x + 2 < len(m) and y < len(m) and m[y][x] == 0 and m[y][x+1] == 0 and m[y][x+2] == 0:
			return True
		else:
			return False
	else:
		if x - 2 >= 0 and y < len(m) and m[y][x] == 0 and m[y][x-1] == 0 and m[y][x-2] == 0:
			return True
		else:
			return False



f = open ( 'matrix1' , 'r')
m = [ map(int,line.split(',')) for line in f ]
visited = []

length = 0
for x in xrange(0,len(m)):
	for y in xrange(0,len(m)):
		[l1,l2] = [0,0]
		if not [x,y,1] in visited:
			print [x,y,1]
			[l1, newVisit] = recursive(x,y,m,visited,0, 1)
			visited.append(newVisit)
		if not [x,y,-1] in visited:
			print [x,y,-1]
			[l2, newVisit] = recursive(x,y,m,visited,0, -1)
			visited.append(newVisit)
		l = max(l1,l2)
		length = max(length,l)
		pass
	pass
print length