import cv2
import os
import random

#cv2.samples.create_samples()

pasta_entrada = 'C:\CODE\Projeto_Robo_tinik\Robot-fish\Codigos\Haar_Cascade\imagens\com_peixe'
pasta_saida = 'C:\CODE\Projeto_Robo_tinik\Robot-fish\Codigos\Haar_Cascade\positivas'

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

def ajustar_brilho(img):
    fator_brilho = random.uniform(0.1, 2)    
    img = cv2.convertScaleAbs(img, alpha=fator_brilho, beta=0)
    
    return img

def girar_imagem(img):
    angulo = random.choice([0, 90, 180, 270])
    
    if angulo == 90:
        img_rotacionada = cv2.transpose(img)
        img_rotacionada = cv2.flip(img_rotacionada, flipCode=1)
    elif angulo == 180:
        img_rotacionada = cv2.flip(img, flipCode=0)
    elif angulo == 270:
        img_rotacionada = cv2.transpose(img)
        img_rotacionada = cv2.flip(img_rotacionada, flipCode=0)        
    else:
        img_rotacionada = img
    
    return img_rotacionada

contador = 1  # Contador de fotos processadas
limite = 2001  # Limite de 1000 fotos processadas

while contador < limite:
    if contador > limite:
        break
    
    nome_arquivo = random.choice(os.listdir(pasta_entrada))
    caminho_arquivo = os.path.join(pasta_entrada, nome_arquivo)
    
    img = cv2.imread(caminho_arquivo)
    img = cv2.resize(img, (200, 200))
    img = ajustar_brilho(img)
    img = girar_imagem(img)
    imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    novo_nome = f'{contador}.png'  
    
    caminho_saida = os.path.join(pasta_saida, novo_nome)
    cv2.imwrite(caminho_saida, imagem_cinza)
    
    contador += 1 
