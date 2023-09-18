import os
import cv2

caminho_imagem = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\imagens\peixe\peixe.png'

if os.path.exists(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    if imagem is not None:
        imagem_redimensionada = cv2.resize(imagem, (200, 200))
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        caminho_saida = os.path.join('C:\CODE\Robot-fish\Codigos\Haar_Cascade', 'mask.png')
        cv2.imwrite(caminho_saida, imagem_cinza)
        print("Processamento concluído.")
    else:
        print("Não foi possível ler a imagem.")
else:
    print(f"O arquivo '{caminho_imagem}' não foi encontrado.")
