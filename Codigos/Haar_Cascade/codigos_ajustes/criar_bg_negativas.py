import os

# Pasta que contém as imagens de fundo negativo
pasta_negativas = 'C:\CODE\Robot-fish\Fotos_Aquario\_negativas'

# Lista de arquivos na pasta de negativas
arquivos_negativas = os.listdir(pasta_negativas)

# Caminho para o arquivo bg.txt
arquivo_bg = 'C:\CODE\Robot-fish\Fotos_Aquario\_negativas/bg.txt'

# Abra o arquivo bg.txt em modo de escrita
with open(arquivo_bg, 'w') as f:
    # Escreva os caminhos dos arquivos de negativas no arquivo bg.txt
    for arquivo in arquivos_negativas:
        caminho_completo = os.path.join(pasta_negativas, arquivo)
        f.write(caminho_completo + '\n')

print(f'O arquivo {arquivo_bg} foi criado com sucesso com {len(arquivos_negativas)} imagens de fundo negativo.')
