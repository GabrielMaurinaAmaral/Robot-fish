  

# Abra o arquivo bg.txt e leia as informações do fundo negativo
with open(arquivo_bg, 'r') as file:
    background_images = file.readlines()

# Certifique-se de que o número de amostras positivas não exceda o número de imagens de fundo disponíveis
num_amostras_positivas = min(num_amostras_positivas, len(background_images))

# Crie um arquivo Positivas.lst para salvar as informações da amostra positiva
with open(arquivo_positivas_lst, 'w') as file:
    for i in range(num_amostras_positivas):
        # Escolha aleatoriamente uma imagem de fundo negativo
        background_image_path = background_images[i].strip()
        
        # Leitura da imagem de fundo negativo
        background_image = cv2.imread(background_image_path)
        
        # Certifique-se de que as dimensões da imagem positiva não excedam as dimensões da imagem de fundo
        h, w, _ = background_image.shape
        max_height, max_width, _ = imagem.shape
        if h > max_height or w > max_width:
            continue
        
        # Crie uma região de interesse (ROI) na imagem de fundo negativo usando a imagem positiva
        x = np.random.randint(0, max_width - w)
        y = np.random.randint(0, max_height - h)
        roi = background_image[y:y+h, x:x+w]
        
        # Copie a imagem positiva na ROI da imagem de fundo negativo
        roi[:h, :w] = imagem
        
        # Salve a imagem resultante como uma amostra positiva
        arquivo_amostra_positiva = f'Positivas/amostra_{i}.png'
        cv2.imwrite(arquivo_amostra_positiva, background_image)
        
        # Escreva as informações da amostra positiva no arquivo Positivas.lst
        linha = f'{arquivo_amostra_positiva} 1 0 0 {w} {h}\n'
        file.write(linha)

print(f'{num_amostras_positivas} amostras positivas criadas com sucesso em {arquivo_positivas_lst}.')
