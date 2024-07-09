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



    #def __getattr__(self, attr):
    #    return self[attr]

#SyntaxError("closing parenthesis ')' does not match opening parenthesis '['", ('<string>', 1, 39, "{'x': array([623.60626, 63...e=float32), 'y': array([137.0182 , 12...e=float32), 'error': None, 'nariz': [623.60626, 137.0182], 'hombroI': [682.09265, 207.9484], 'hombroD': [571.8314, 202.1973], 'cuello': [626.9620361328125, 205.07284545898438], 'angCuelloSupI': 95.80874409528306, 'angCuelloSupD': 84.19125590471695, 'codoI': [697.43335, 293.25632], 'codoD': [547.8615, 285.58823], 'manoI': [696.4746, 365.14505], 'manoD': [532.5208, 362.2695], 'angCodoI': 190.95845977843885, ...}", 1, 39))