import cv2
import numpy as np

# Caminho para o arquivo info.lst com a lista de imagens positivas
info_file = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\info.dat'

# Nome do arquivo vector positivo de saída
output_vec_file = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\positivas.vec'

# Tamanho das amostras
width, height = 20, 20

# Número de amostras
num_samples = 2000

# Crie uma lista para armazenar as amostras de imagem
samples = []

# Abra o arquivo info.lst e leia as informações das imagens positivas
with open(info_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 6:
            img_file = parts[0]
            x, y, w, h = map(int, parts[2:6])
            img = cv2.imread(img_file, 0)  # Carrega a imagem em escala de cinza
            roi = img[y:y+h, x:x+w]  # Recorta a região de interesse (ROI)
            roi_resized = cv2.resize(roi, (width, height))  # Redimensiona a ROI para o tamanho desejado
            samples.append(roi_resized)

# Verifique se temos amostras suficientes
if len(samples) < num_samples:
    print("Número insuficiente de amostras positivas.")
    exit()

# Crie o arquivo vector positivo
output_file = cv2.FileStorage(output_vec_file, cv2.FILE_STORAGE_WRITE)
output_file.write('images', np.array(samples))
output_file.release()

print(f"Arquivo vector positivo {output_vec_file} criado com sucesso.")
