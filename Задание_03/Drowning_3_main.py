#dist-distance r-Rescuer w-water_line D-drowning ldispl-lateral_displacement(боковое смещение) 
import math
from Drowning_3_input import distRw, distDw, ldispl, vsand, nslow
from Drowning_3_fn import path_length, time_path 



ytof = 3 #преобразование ярдов в футы (в одном ярде три фута)


optimal_time_teta ={} #словарь для складывания пар 'угол:время спасения'
teta_deg = 0 #значния угла в градусах
while teta_deg<89.9:
	teta_deg+=0.1
	
	#teta_list1.append(teta_deg)
	teta_r = teta_deg*math.pi/180
	xdist = (distRw *ytof)* math.tan(teta_r) # в футах

	L1dist = path_length (distRw*ytof, xdist) # в футах
	L2dist = path_length ((ldispl*ytof - xdist), distDw ) #в футах

	#vswim = vsand/n
	# преобразование скорости в футов/сек
	vsand_fs = vsand*(5280/3600)
	vswim_fs = vsand_fs/nslow

	time_sand = time_path(L1dist, vsand_fs)
	time_water = time_path(L2dist, vswim_fs)

	

	timeResque = time_sand + time_water
	optimal_time_teta[teta_deg] = timeResque
'''
Показать все значения
for teta, time in optimal_time_teta.items():
    print(f"{teta:.2f} : {time:.3f}")
'''
best_teta = min(optimal_time_teta, key=optimal_time_teta.get)
best_time = optimal_time_teta[best_teta]

print(f"Оптимальный угол = {best_teta:.2f} за минимальное время = {best_time:.3f} секунд")








