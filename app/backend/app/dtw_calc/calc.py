import pandas as pd
from app.dtw_calc.normalization import normalize_angles, normalize_positions
from app.dtw_calc.dtw_angle import distance_dtw_angles
from app.dtw_calc.dtw_pos import distance_dtw_pos

body_names = ['nariz', 'cuello', 'hombroI', 'hombroD',
       'codoI', 'codoD', 'manoI', 'manoD', 'caderaI', 'caderaD',
       'caderaM', 'rodillaI', 'rodillaD', 'tobilloI', 'tobilloD']


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

def compare(file1, file2, positions= body_names, angles = angles_names):
   
    data1 = pd.read_pickle(file1)
    data2 = pd.read_pickle(file2)

    normalize_angles(data1, angles)
    normalize_angles(data2, angles)

    normalize_positions(data1, positions)
    normalize_positions(data2, positions)

    distance1 = distance_dtw_angles(data1, data2)
    distance2 = distance_dtw_pos(data1, data2, positions)

    return distance2

def get_default_names():
    return body_names, angles_names

