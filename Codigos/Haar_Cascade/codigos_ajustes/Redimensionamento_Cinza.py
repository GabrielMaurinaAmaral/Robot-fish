import os
import cv2

pasta_entrada = 'C:\CODE\Robot-fish\Fotos_Aquario\Positivas'
pasta_saida = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\Positivas'

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

extensoes = ['jpg', 'jpeg', 'png']
contador = 1

for arquivo in os.listdir(pasta_entrada):
    if arquivo.lower().endswith(tuple(extensoes)):
        caminho_completo = os.path.join(pasta_entrada, arquivo)
        imagem = cv2.imread(caminho_completo)
        imagem_redimensionada = cv2.resize(imagem, (640, 480))
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        novo_nome = f'{contador}.png'  
        caminho_saida = os.path.join(pasta_saida, novo_nome)
        cv2.imwrite(caminho_saida, imagem_cinza)        
        contador += 1  

print("Processamento concluído.")
