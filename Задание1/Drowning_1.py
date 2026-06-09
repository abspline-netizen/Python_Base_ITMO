#dist-distance r-Rescuer w-water_line D-drowning ldispl-lateral_displacement(боковое смещение) dirm-direction_of_movement
import math

distRw = float(input('Введите кратчайшее расстояние от спасателя до кромки воды, d1 (в ярдах)'))
distDw = float(input('Введите кратчайшее расстояние от утопающего до берега, d2 (в футах)'))
ldispl = float(input('Введите боковое смещение между спасателем и утопающим, h (в ярдах)'))
vsand = float(input('Скорость движения спасателя по песку, vsand (в милях в час)'))
nslow = float(input('Введите коэффициент замедления спасателя при движении в воде, n'))
dirm = float(input('Направление движения спасателя по песку, θ1 (в градусах)'))


# в одном ярде три фута, а в одной миле 5280 футов
# преобразование градусов в радианы (1° × π/180) = 0,01745 рад
dirm_r = dirm*math.pi/180


#x = d1·tan(θ1)
xdist = (distRw *3)* math.tan(dirm_r) #distRw *3 - преобразование в футы


L1dist = math.sqrt(xdist**2 + (distRw*3)**2)
L2dist = math.sqrt((ldispl*3-xdist)**2+(distDw)**2) #ldispl*3- преобразование в футы


#vswim = vsand/n
# преобразование скорости в футов/сек
vsand_fs = vsand*(5280/3600)
timeResque = (1/vsand_fs)*(L1dist + L2dist*nslow)
print(f'Если спасатель начнет движение под углом θ1, равным {dirm:.0f} градусов, он достигнет утопающего через {timeResque:.1f} секунд')