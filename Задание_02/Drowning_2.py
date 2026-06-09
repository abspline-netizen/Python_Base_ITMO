#dist-distance r-Rescuer w-water_line D-drowning ldispl-lateral_displacement(боковое смещение) 
import math

distRw = float(input('Введите кратчайшее расстояние от спасателя до кромки воды, d1 (в ярдах)'))
distDw = float(input('Введите кратчайшее расстояние от утопающего до берега, d2 (в футах)'))
ldispl = float(input('Введите боковое смещение между спасателем и утопающим, h (в ярдах)'))
vsand = float(input('Скорость движения спасателя по песку, vsand (в милях в час)'))
nslow = float(input('Введите коэффициент замедления спасателя при движении в воде, n'))
teta = float(input('Направление движения спасателя по песку, θ1 (в градусах)'))

# в одном ярде три фута, а в одной миле 5280 футов
# преобразование градусов в радианы (1° × π/180) = 0,01745 рад
teta_r = teta*math.pi/180

#x = d1·tan(θ1)
xdist = (distRw *3)* math.tan(teta_r) #distRw *3 - преобразование в футы

#определение длины пути
def path_length (side_dist1, side_dist2):
    path = math.sqrt((side_dist1**2) + (side_dist2**2))
    return path

L1dist = path_length (distRw*3, xdist)
L2dist = path_length ((ldispl*3 - xdist), distDw ) #ldispl*3- преобразование в футы

#vswim = vsand/n
# преобразование скорости в футов/сек
vsand_fs = vsand*(5280/3600)
vswim_fs = vsand_fs/nslow
#определение времени пути 
def time_path (path, velosity):
    time = path/velosity
    return time

time_sand = time_path(L1dist, vsand_fs)
time_water = time_path(L2dist, vswim_fs)

timeResque = time_sand + time_water
print(f'Если спасатель начнет движение под углом θ1, равным {teta:.0f} градусов, он достигнет утопающего через {timeResque:.1f} секунд')
