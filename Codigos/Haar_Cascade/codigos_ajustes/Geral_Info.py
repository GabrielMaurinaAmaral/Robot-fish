import os

pasta_negativas = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\_negativas'
pasta_positivas = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\positivas'

arquivo_bg = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\_bg.txt'
arquivo_info = 'C:\CODE\Robot-fish\Codigos\Haar_Cascade\info.list'

arquivos_negativas = os.listdir(pasta_negativas)
arquivos_positivas = os.listdir(pasta_positivas)

with open(arquivo_bg, 'w') as bg_arquivo:
    for arquivo in arquivos_negativas:
        caminho_completo = os.path.join(pasta_negativas, arquivo)
        bg_arquivo.write(caminho_completo + '\n')
        
with open(arquivo_info, 'w') as info_arquivo:
    for arquivo in arquivos_positivas:
        caminho_completo = os.path.join(pasta_positivas, arquivo)
        linha = f'{caminho_completo} 1 0 0 200 200\n'
        info_arquivo.write(linha)
