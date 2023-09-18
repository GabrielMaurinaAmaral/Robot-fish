import numpy as np
import cv2
import os

igual = False

for file_type in ['negativas']:
    for img in os.listdir(file_type):
        for feia in os.listdir('feias'):
            try:
                caminho_imagem = str(file_type)+'/'+str(img)
                
                feia = cv2.imread('feias/'+str(feia))
                
                pergunta = cv2.imread(caminho_imagem)
                
                if feia.shape == pergunta.shape and not(np.bitwise_xor(feia,pergunta).any()):
                    print('Apagando imagem feia!')
                    print(caminho_imagem)
                    os.remove(caminho_imagem)
            
            except Exception as e:
                print(str(e))