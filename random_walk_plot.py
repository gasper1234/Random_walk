from random_walk import *
import matplotlib.pyplot as plt

M = 10000
N = 10000
mi = 2

#priemr za računanje gamma
'''
t, mad = M_N_flight(M, N, mi)
t_log = []
mad_log = []
for j in range(1, len(t)):
	t_log.append(np.log(t[j]))
	mad_log.append(np.log(mad[j]))
plt.plot(t_log, mad_log, 'x')
plt.plot(t_log, linfit(t_log, mad_log)(t_log), 'r-')
plt.ylabel(r'$\log(\rm{MAD(t)})$')
plt.xlabel(r'$\log(t)$')
plt.show()
'''
# računanje difuzije

mi_list = [1.2, 1.5, 1.7, 2, 2.5, 3, 4, 6]
gamma_flight = []
gamma_walk = []


for i in mi_list:
	t, mad = M_N_flight(M, N, i)
	t_log = []
	mad_log = []
	for j in range(1, len(t)):
		t_log.append(np.log(t[j]))
		mad_log.append(np.log(mad[j]))
	gamma_flight.append(np.polyfit(t_log, mad_log, 1, full = True)[0][0])

	t, mad = M_N_walk(M, N, i)
	t_log = []
	mad_log = []
	for j in range(1, len(t)):
		t_log.append(np.log(t[j]))
		mad_log.append(np.log(mad[j]))
	gamma_walk.append(np.polyfit(t_log, mad_log, 1, full = True)[0][0])

print(gamma_walk)
print(gamma_flight)
print(mi_list)



#sprehodi ploti

'''

fig, axs = plt.subplots(2, 2)
N = 10
x, y = x_y_data(N+1, mi, walk)
axs[0, 0].plot(x, y)
axs[0, 0].axis('equal')
axs[0, 0].ticklabel_format(style = 'sci')
axs[0, 0].set_title('N='+str(N))
N = 100
x, y = x_y_data(N+1, mi, walk)
axs[0, 1].plot(x, y)
axs[0, 1].axis('equal')
axs[0, 1].ticklabel_format(style = 'sci')
axs[0, 1].set_title('N='+str(N))
N = 1000
x, y = x_y_data(N+1, mi, walk)
axs[1, 0].plot(x, y)
axs[1, 0].axis('equal')
axs[1, 0].ticklabel_format(style = 'sci')
axs[1, 0].set_title('N='+str(N))
N = 10000
x, y = x_y_data(N+1, mi, walk)
axs[1, 1].plot(x, y)
axs[1, 1].axis('equal')
axs[1, 1].ticklabel_format(style = 'sci')
axs[1, 1].set_title('N='+str(N))
plt.show()

'''
