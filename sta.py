import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def ave(x):
	re = 0
	for i in x:
		re += i
	return re/len(x)

def linfit(x, y):
	fit = np.polyfit(x, y, 1, full = True)
	print('naklon premice in zač. vr.:', fit[0][0], fit[0][1])
	sq = fit[1][0]/sqrt(len(x)-2)
	pov = ave(x)
	sx = 0
	for i in x:
		sx += (pov - i) ** 2
	sx = sqrt(sx)
	if sx != 0:
		sq /= sx
		print('abs. napaka naklona:', sq)
		print('rel. napaka naklona', sq/fit[0][0])
	else:
		print('povprečje x ravno 0!')
	fit = np.polyfit(x, y, 1)
	return np.poly1d(fit)
