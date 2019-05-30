import imageio
import matplotlib.pyplot as plt
import numpy as np
def reglaAutomataUno(subMatrix, elementoCentral):
    size = subMatrix.shape
    Ceros = 0
    Unos = 0
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if(subMatrix[i][j] == 0):
                Ceros += 1
            else:
                Unos += 1
    if(elementoCentral == 0 and Ceros == 3):
        return 255
    elif(elementoCentral != 0 and (Unos == 2 or Unos == 3)):
        return 255
    else:
        return 0

def reglaAutomataDos(subMatrix, elementoCentral):
    size = subMatrix.shape
    Ceros = 0
    Unos = 0
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if(subMatrix[i][j] == 0):
                Ceros += 1
            else:
                Unos += 1
    if(elementoCentral == 0 and (Ceros>= 3 and Ceros<= 4)):
        return 255
    elif(elementoCentral != 0 and (Unos>= 2 and Unos<= 5)):
        return 255
    else:
        return 0
def correrIteracionPrimerAutomata(I0):
    size = I0.shape
    redimI0 = np.zeros(shape=(size[0] + 2, size[1] + 2))
    size = redimI0.shape
    redimI0[1:size[0] - 1, 1: size[1] - 1] = I0
    matrixIteracionPrimerRegla = np.zeros(shape = (size[0], size[1]))
    matrixIteracionSegundaRegla = np.zeros(shape = (size[0], size[1]))
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if(i >= 1 and j>= 1):
                subMatrix = redimI0[i-1:i+2,j-1:j+2]
                matrixIteracionPrimerRegla[i][j] = reglaAutomataUno(subMatrix, redimI0[i][j])
    return matrixIteracionPrimerRegla

def correrIteracionSegundoAutomata(I0):
    size = I0.shape
    redimI0 = np.zeros(shape=(size[0] + 2, size[1] + 2))
    size = redimI0.shape
    redimI0[1:size[0] - 1, 1: size[1] - 1] = I0
    matrixIteracionPrimerRegla = np.zeros(shape = (size[0], size[1]))
    matrixIteracionSegundaRegla = np.zeros(shape = (size[0], size[1]))
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if(i >= 1 and j>= 1):
                subMatrix = redimI0[i-1:i+2,j-1:j+2]
                matrixIteracionPrimerRegla[i][j] = reglaAutomataDos(subMatrix, redimI0[i][j])
    return matrixIteracionPrimerRegla

Img = imageio.imread('lena.png')
I0 = Img[:,:,0].astype(np.float64)
I1 = Img[:,:,0].astype(np.float64)
for i in range(0, 50):
    I0 = correrIteracionPrimerAutomata(I0) 
    I1 = correrIteracionSegundoAutomata(I1)
    
imageio.imwrite("PrimerAutomataLena.png", I0)
imageio.imwrite("SegundoAutomataLena.png", I1)
