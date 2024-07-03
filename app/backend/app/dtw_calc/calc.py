import pandas as pd


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



def get_default_names():
    return body_names, angles_names

