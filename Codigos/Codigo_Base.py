import cv2
COR_VERMELHO = (0,0,255)
COR_VERDE = (0,255,0)
COR_AZUL = (255,0,0)


class Rastreamento_Peixe:
    def __init__(self):
        self.kernel_size = (5, 5)
        self.epsilon_multiplicador = 0.001
        self.range_cor = [(0, 0, 0), (255, 50, 50)]
        
    def linearizar_frame(self, frame):      
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
        black_mask = cv2.inRange(hsv, self.range_cor[0], self.range_cor[1])    
        black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
        gray_frame = cv2.cvtColor(black_result, cv2.COLOR_BGR2GRAY)  
        gaus_frame = cv2.GaussianBlur(gray_frame, self.kernel_size, 0)
        _, frame_binario = cv2.threshold(gaus_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        pixel_preenchimento = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernel_size)
        frame = cv2.morphologyEx(frame_binario, cv2.MORPH_CLOSE, pixel_preenchimento)
        return frame
    
    def trancking_peixe(self, frame, frame_binario):
        contornos, _= cv2.findContours(frame_binario, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contornos:
            max_Area = cv2.contourArea(contornos[0])
            contorno_Max_Area_Id = 0
            for i, contorno in enumerate(contornos):
                if max_Area < cv2.contourArea(contorno):
                    max_Area = cv2.contourArea(contorno)
                    contorno_Max_Area_Id = i
            maior_Contorno = contornos[contorno_Max_Area_Id]
            epsilon = self.epsilon_multiplicador * cv2.arcLength(maior_Contorno, True)
            aprox = cv2.approxPolyDP(maior_Contorno, epsilon, True)
            cv2.drawContours(frame, [aprox], -1, (0,255,255), 1)
            h_Frame, w_Frame, _ = frame.shape
            x_Contorno, y_Contorno, w_Contorno, h_Contorno = cv2.boundingRect(maior_Contorno)            
            x_Central, y_Central = x_Contorno + int(w_Contorno / 2), y_Contorno + int(h_Contorno / 2)
            cv2.circle(frame, (int(w_Frame/2), int(h_Frame/2)), 5, COR_AZUL, -1)
            cv2.circle(frame, (x_Central, y_Central), 5, COR_VERMELHO, -1)
            cv2.rectangle(frame, (x_Contorno, y_Contorno), (x_Contorno + w_Contorno, y_Contorno + h_Contorno), COR_VERMELHO, 2)
            cv2.line(frame, (int(w_Frame/2), int(h_Frame/2)), (x_Central, y_Central), COR_VERDE, 1)

    def main(self):
        webcam = cv2.VideoCapture(0)
        while True:
            valido, frame = webcam.read()
            if valido:           
                frame_binario = self.linearizar_frame(frame)
                self.trancking_peixe(frame, frame_binario)
                cv2.imshow('PRINCIPAL', frame)     
                if cv2.waitKey(1) != -1:
                    break
            else:
                break    
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    tracker = Rastreamento_Peixe()
    tracker.main()