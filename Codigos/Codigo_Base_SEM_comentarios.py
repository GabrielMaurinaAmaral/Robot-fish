import cv2

COR_VERMELHO = (0, 0, 255)
COR_VERDE = (0, 255, 0)
COR_AZUL = (255, 0, 0)

LIMITE_INFERIOR = (90, 50, 50) 
LIMITE_SUPERIOR = (130, 255, 255) 


class Rastreamento_Peixe:

    def __init__(self):
        self.kernel_size = (5, 5)
        self.epsilon_multiplicador = 0.001
        self.range_cor = [LIMITE_INFERIOR, LIMITE_SUPERIOR]

    def linearizar_frame(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        black_mask = cv2.inRange(hsv, self.range_cor[0], self.range_cor[1])
        black_result = cv2.bitwise_and(frame, frame, mask=black_mask)
        gray_frame = cv2.cvtColor(black_result, cv2.COLOR_BGR2GRAY)
        gaus_frame = cv2.GaussianBlur(gray_frame, self.kernel_size, 0)
        _, frame_binario = cv2.threshold(gaus_frame, 0, 255, cv2.THRESH_BINARY)
        pixel_preenchimento = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernel_size)
        frame = cv2.morphologyEx(frame_binario, cv2.MORPH_CLOSE, pixel_preenchimento)
        return frame

    def trancking_peixe(self, frame, frame_binario):
        contornos, _ = cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contornos:
            max_Area = cv2.contourArea(contornos[0])
            contorno_Max_Area_Id = 0
            for i, contorno in enumerate(contornos):
                if max_Area < cv2.contourArea(contorno):
                    max_Area = cv2.contourArea(contorno)
                    contorno_Max_Area_Id = i
            maior_Contorno = contornos[contorno_Max_Area_Id]
            self.desenha_grade(frame)
            self.desenha_trancking(frame, maior_Contorno)

    def desenha_trancking(self, frame, contorno):
        hull = cv2.convexHull(contorno)
        cv2.drawContours(frame, [hull], -1, COR_AZUL, 1)
        M = cv2.moments(hull)
        x_Central = int(M["m10"] / M["m00"])
        y_Central = int(M["m01"] / M["m00"])
        cv2.circle(frame, (x_Central, y_Central), 5, COR_VERMELHO, -1)
        cv2.drawContours(frame, [contorno], -1, (0, 255, 255), 1)
        texto = f"X: {x_Central}, Y: {y_Central}"
        cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        
    def desenha_grade(self, frame):
        h_Frame, w_Frame, _ = frame.shape
        divisoes = 3
        for i in range(1, divisoes):
            y = int(i * h_Frame / divisoes)
            cv2.line(frame, (0, y), (w_Frame, y), COR_VERDE, 2)
        for i in range(1, divisoes):
            x = int(i * w_Frame / divisoes)
            cv2.line(frame, (x, 0), (x, h_Frame), COR_VERDE, 2)

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
