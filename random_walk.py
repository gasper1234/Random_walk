import random as rd
import numpy as np
from scipy.stats import median_abs_deviation
from sta import *


def random_dist(mi):
	a = 1
	rho = rd.random()
	return a * rho ** (1 / (1-mi))

def step(mi):
	t = random_dist(mi)
	fi = rd.random()*np.pi*2
	pos = [t * np.cos(fi), t * np.sin(fi), t]
	return pos

def walk(N, mi):
	sez = [[0, 0, 0] for i in range(N)]
	for i in range(1, N):
		one_step = step(mi)
		sez[i] = [sez[i-1][j]+one_step[j] for j in range(3)]
	return sez

def r(pos):
	return np.sqrt( pos[0] ** 2 + pos[1] ** 2 )

def M_N_walk(M, N, mi):

	t_labels = [t/100 * N for t in range(100)]
	mad_tabel = [0 for _ in range(100)]
	mad_calc = [0 for _ in range(M)]

	end_pos_p = [[0, 0, 0] for _ in range(M)]
	end_pos_r = [[0, 0, 0] for _ in range(M)]

	for i in range(100):
		for j in range(M):
			while end_pos_r[j][2] < t_labels[i]:
				one_step = step(mi)
				end_pos_r[j] = [end_pos_p[j][k]+one_step[k] for k in range(3)]
				end_pos_p[j] = end_pos_r[j]
			D_t_0 = (end_pos_r[j][2]-end_pos_p[j][2])
			if D_t_0 == 0:
				delta_rel = 0
			else:
				delta_rel = (t_labels[j]-end_pos_p[j][2]) / D_t_0
			delta_x = end_pos_p[j][0] + delta_rel * (end_pos_r[j][0] - end_pos_p[j][0])
			delta_y = end_pos_p[j][1] + delta_rel * (end_pos_r[j][1] - end_pos_p[j][1])
			mad_calc[j] = np.sqrt( delta_x ** 2 + delta_y ** 2 )
		mad_tabel[i] = median_abs_deviation(mad_calc)
	return t_labels, mad_tabel

def flight(N, mi):
	sez = [[0, 0, 0] for i in range(N)]
	for i in range(1, N):
		one_step = step(mi)
		sez[i] = [sez[i-1][j]+one_step[j] for j in range(2)]
	return sez

def M_N_flight(M, N, mi):

	t_labels = [int(round(t / 100 * N)) for t in range(100)]
	mad_tabel = [0 for _ in range(100)]
	mad_calc = [0 for _ in range(M)]

	end_pos_p = [[0, 0, 0] for _ in range(M)]
	end_pos_r = [[0, 0, 0] for _ in range(M)]

	for i in range(N):
		for j in range(M):
			one_step = step(mi)
			end_pos_r[j] = [end_pos_p[j][k]+one_step[k] for k in range(2)]
			end_pos_p[j] = end_pos_r[j]
			if i in t_labels:
				delta_x = end_pos_r[j][0]
				delta_y = end_pos_r[j][1]
				mad_calc[j] = np.sqrt( delta_x ** 2 + delta_y ** 2 )
		if i in t_labels:
			for k in range(100):
				if i == t_labels[k]:
					mad_tabel[k] = median_abs_deviation(mad_calc)
					break
	return t_labels, mad_tabel

def x_y_data(N, mi, f):
	m_f = f(N, mi)
	x = [0 for _ in range(N)]
	y = [0 for _ in range(N)]
	for i in range(N):
		x[i] = m_f[i][0]
		y[i] = m_f[i][1]
	return x, y