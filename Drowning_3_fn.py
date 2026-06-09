#dist-distance r-Rescuer w-water_line D-drowning ldispl-lateral_displacement(боковое смещение) 
import math



#определение длины пути
def path_length (side_dist1, side_dist2):
    path = math.sqrt((side_dist1**2) + (side_dist2**2))
    return path




#определение времени пути 
def time_path (path, velosity):
    time = path/velosity
    return time


