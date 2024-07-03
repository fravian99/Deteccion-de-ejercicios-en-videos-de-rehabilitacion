import numpy as np
from dtaidistance import dtw

angles_names = [
    'angCuelloI',
    'angCuelloD', 
    'angCodoI', 
    'angCodoD', 
    'angHombroI', 
    'angHombroD',
    'angCaderaI', 
    'angCaderaD', 
    'angCaderaTorsoI', 
    'angCaderaTorsoD',
    'angRodillaI', 
    'angRodillaD'
    ]

def dtwdis_angles(angles1, angles2):
    return dtw.distance(angles1, angles2)

def distance_dtw_angles_with_distances(points1, points2, custom_names = None):
    distances = []
    actual_angles = angles_names if custom_names is None else custom_names  
    for angle_name in actual_angles:
        angles1 = np.asarray(points1[angle_name])
        angles2 = np.asarray(points2[angle_name])

        actual_distance = dtwdis_angles(angles1, angles2)
        #print(angle_name, " ", actual_distance)
        
        distances.append(actual_distance)
    #print(distance)
    return distances

def distance_dtw_angles(points1, points2, custon_names = None):
    distances = distance_dtw_angles_with_distances(points1, points2, custon_names)
    distance = np.mean(distances)
    score = distance
    return score