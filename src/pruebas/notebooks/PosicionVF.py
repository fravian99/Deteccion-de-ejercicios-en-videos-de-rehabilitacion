import numpy as np
# Solucion temporal al error relacionado con los nuevos archivos de datos
class Posicion():
    angCuelloI: float
    angCuelloD: float
    angCodoI: float
    angCodoD: float
    angHombroI: float
    angHombroD: float
    angCaderaI: float
    angCaderaD: float
    angCaderaTorsoI: float
    angCaderaTorsoD: float
    angRodillaI: float
    angRodillaD: float
    pass
    def __init__(self,a):
       self.angCuelloD = a.angCuelloSupD
       self.angCuelloI = a.angCuelloSupI
       self.angCodoI = a.angCodoI
       self.angCodoD = a.angCodoD
       self.angHombroI = a.angHombroI
       self.angHombroD = a.angHombroD
       self.angCaderaI = a.angCaderaI
       self.angCaderaD = a.angCaderaD
       self.angCaderaTorsoI = a.angCaderaTorsoI
       self.angCaderaTorsoD = a.angCaderaTorsoD
       self.angRodillaI = a.angRodillaI
       self.angRodillaD = a.angRodillaD


