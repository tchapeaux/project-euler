import math
iterator = 0
triangle = 0
while(True):
	iterator += 1
	triangle += iterator
	divtest = 0
	divcount = 0
	while(divtest <= triangle):
		divtest += 1
		if (triangle % divtest == 0):
			divcount += 1
	if (triangle % 100000 == 0):
		print triangle, divcount
	if (divcount > 500):
		break
print triangle