import numpy as np
from dtaidistance import dtw

def dtwdistance(user1, user2):
    array1 = np.asarray(user1).astype('float64').reshape(2*len(user1),)
    array2 = np.asarray(user2).astype('float64').reshape(2*len(user2),)
    distance = dtw.distance_fast(array1, array2)
    return distance

def get_score(distance):
    return 100- 100*distance

def distance_dtw_pos(profesional, patient, used_coords_names):
    """
    Devuelve la puntuacion DTW segun las coordenadas
    """
    temp = []
    used_coords_distance = 0

    for coord_name in used_coords_names:
        coord_names = [coord_name+"_x", coord_name+"_y"]
        distance = dtwdistance(profesional[coord_names], patient[coord_names])
        temp.append(distance)
        used_coords_distance += distance
    
    used_distance = used_coords_distance/len(used_coords_names)
    return get_score(used_distance)
