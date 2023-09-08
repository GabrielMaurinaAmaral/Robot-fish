import cv2
COR_VERMELHO = (0,0,255)
COR_VERDE = (0,255,0)
COR_AZUL = (255,0,0)
# Criação do Objeto para ter maior controle de funções e variaveis
class Rastreamento_Peixe:
    # Contrutor com variarveis inportantes para linearização
    def __init__(self):
        self.kernel_size = (5, 5) # Determina o tamanho do pixel que sera usado para prencher pequenos espaçoes vazios dentro do contorno
        self.epsilon_multiplicador = 0.001 # Quanto +proximo do sero, mais detalhado sera o desenho do contorno 
        self.range_cor = [(0, 0, 0), (255, 50, 50)] # Intervalo escolhirdo de cor hsv para ser detectados
    # Função que lineariza a imagem para que fica apenas pixel com valor de 0 ou 1.
    # Onde um pixel que eram da tonalidade escura e 0 qualquer outra cor que não estava o internalo determinado por range_cor
    def linearizar_frame(self, frame):      
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Converte d frame de BGR para HVS
        black_mask = cv2.inRange(hsv, self.range_cor[0], self.range_cor[1]) # Converte em 1 quem esta no intervalo e quem não esta fica 0 
        black_result= cv2.bitwise_and(frame, frame, mask=black_mask) # Pega o frame original e usa o black_mask para passar os pixels que estão com1   
        gray_frame = cv2.cvtColor(black_result, cv2.COLOR_BGR2GRAY)  # Converte para tons de cinza o resultado da mascara 
        gaus_frame = cv2.GaussianBlur(gray_frame, self.kernel_size, 0) # Defoca a imagem, para que temnha mais pontos unindo o contorno, com intuido que fique mais constante o contorno
        _, frame_binario = cv2.threshold(gaus_frame, 0, 255, cv2.THRESH_BINARY) # Converte em binario
        pixel_preenchimento = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernel_size) # Cria um pixel em forma de cruz
        frame = cv2.morphologyEx(frame_binario, cv2.MORPH_CLOSE, pixel_preenchimento) # Substitui os pixel pelo pixel de preenchimento, afim de fiminuir o ruido
        return frame
    # Pega o frame original e por meio do frame binario cria um trackin fo frame  determinado
    def trancking_peixe(self, frame, frame_binario):
        contornos, _= cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # agrupo em uma matriz todos os contorno(grupos de com dados 1)
        if contornos: # se existir algum contorno no frame_binario detectado
            max_Area = cv2.contourArea(contornos[0]) # Determinna o priemeiro contorno como maior contorno
            contorno_Max_Area_Id = 0 # Mesma coisa com  id do contorno maximo
            for i, contorno in enumerate(contornos): # Vai percorrer dos os contornos obtidos, afim de acgar o maior contorno
                if max_Area < cv2.contourArea(contorno): # Verefica se um maior contorno foi encontrado
                    max_Area = cv2.contourArea(contorno) # Se foi achado atribui ele a novo maior contorno
                    contorno_Max_Area_Id = i # O meso é feito com id, salva o id do maior contorno
            maior_Contorno = contornos[contorno_Max_Area_Id] # Apos percorrer todos os frames do contorno, era ser atribuido a varivael que sera utilizada
            self.desenha_trancking(frame, maior_Contorno)  # A partir desse maior contorno encontrado, desenha as informaçoes na tela
            self.desenha_grade(frame) # Quase a mesma coisa, mas desenha partes que não seram inportantes pra o resultado final, mas da detalhes do funcionamento
    #
    def desenha_trancking(self, frame, contorno):
        # Encontre o retângulo convexo em torno do contorno
        hull = cv2.convexHull(contorno)
        # Desenha o retângulo convexo no frame
        cv2.drawContours(frame, [hull], -1, COR_AZUL, 1)
        # Encontre o centro do retângulo convexo (pode ser usado como ponto central do contorno)
        M = cv2.moments(hull)
        x_Central = int(M["m10"] / M["m00"])
        y_Central = int(M["m01"] / M["m00"])
        # Desenha um ponto no centro
        cv2.circle(frame, (x_Central, y_Central), 5, COR_VERMELHO, -1)
        # Desenha o contorno 
        cv2.drawContours(frame, [contorno], -1, (0, 255, 255), 1)

    #
    def desenha_grade(self, frame):
        h_Frame, w_Frame, _ = frame.shape 
        divisoes = 3  # Número de divisões ao longo de cada eixo (grade 3x3)
        # Desenha as linhas horizontais da grade
        for i in range(1, divisoes):
            y = int(i * h_Frame / divisoes)
            cv2.line(frame, (0, y), (w_Frame, y), COR_VERDE, 2)
        # Desenha as linhas verticais da grade
        for i in range(1, divisoes):
            x = int(i * w_Frame / divisoes)
            cv2.line(frame, (x, 0), (x, h_Frame), COR_VERDE, 2)
    #
    def loop(self):
        webcam = cv2.VideoCapture(0) 
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        webcam.set(cv2.CAP_PROP_FPS, 30)

        while True:
            valido, frame = webcam.read()
            if valido:           
                frame_binario = self.linearizar_frame(frame)
                self.trancking_peixe(frame, frame_binario)
                cv2.imshow('BINARIO', frame_binario)     
                cv2.imshow('PRINCIPAL', frame)     
                if cv2.waitKey(1) != -1:
                    break
            else:
                break    
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    tracker = Rastreamento_Peixe()
    tracker.loop()