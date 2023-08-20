import time
import cv2
import numpy as np
#tee
# teste de rpg pra hsv depois linariza
def lineanize_black_hsv(frame):    
    # transforma a imagem de bgr em hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # marcador pra saber se o pixel pertence ao intervalo ou não   
    black_mask = cv2.inRange(hsv, (0, 20, 0), (255, 255, 90))
    # aplica máscara que "deixa passar" pixels pertencentes ao intervalo, como filtro
    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
    #lineariza agora para tons de cinza    
    binary_frame = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
    _,binary_frame = cv2.threshold(binary_frame, 0, 255, cv2.THRESH_BINARY)   
    cv2.imshow('Imagem binaria por hsv', binary_frame)
    # tentar diminuir o ruido aomentando os espaços do pixel brancos
    pixel_cover = np.ones((2, 2), np.uint8)
    binary_frame = cv2.dilate(binary_frame, pixel_cover, iterations=10)
    cv2.imshow('Imagem com menos ruido', binary_frame)

    return binary_frame

##teste de rpg pra cinza depois lineariza
#def lineanize_black_gray(frame):
#    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
#    _,gray = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
#    cv2.imshow('Imagem binaria por cinza', gray)
#    return gray

## teste usaando mascara rpg    
#def lineanize_black_bgr(frame): 
#    black_mask = cv2.inRange(frame, (0, 0, 0), (250, 50, 50))
#    # cv2.imshow("MASCARA",black_mask)
#    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
#    cv2.imshow("FRAME - MASCARA",black_result)
#    # aplica linearização
#    gray = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
#    _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
#    cv2.imshow('Imagem binaria por gbr', gray)
#    return gray
    
    
def trancking(frame, hsv):
    #encontra pontos que circundam regiões conexas (contour)
    contours, hierarchy = cv2.findContours(hsv, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #se existir contornos    
    if contours:
        #retornando a área do primeiro grupo de pixels brancos
        max_Area = cv2.contourArea(contours[0])
        contour_Max_Area_Id = 0
        i = 0
        #para cada grupo de pixels branco existente
        for cnt in contours:
            #procura o grupo com a maior área
            if max_Area < cv2.contourArea(cnt):
                max_Area = cv2.contourArea(cnt)
                contour_Max_Area_Id = i
            i += 1
            
        #achei o contorno com maior área em pixels
        cntMaxArea = contours[contour_Max_Area_Id]
        #retorna um retângulo que envolve o contorno em questão
        x_Rect, y_Rect, w_Rect, h_Rect = cv2.boundingRect(cntMaxArea)
        #desenha caixa envolvente com espessura 3
        cv2.rectangle(frame, (x_Rect, y_Rect), (x_Rect + w_Rect, y_Rect + h_Rect), (0, 0, 255), 2)
        cv2.circle(frame, (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), 5, (0, 255, 0), -1)
        
        #desenha o ponto no meio da camera
        height, width, _ = frame.shape

        cv2.circle(frame, (int(width/2), int(height/2)), 5, (255, 0, 0), -1)
        #desenha o vetor do ponto centra da tela a ate o ponto central da regiao detectada        
        frame = cv2.line(frame, (int(width/2), int(height/2)), (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), (0, 255, 0), 2)
    return frame
    
def main():
    webcam = cv2.VideoCapture(0)
    
    while True:
        validacao, frame = webcam.read()
    
        if validacao:           
            
            hsv = lineanize_black_hsv(frame)
            #bgr = lineanize_black_bgr(frame)
            #gray =  lineanize_black_gray(frame)

            frame = trancking(frame, hsv)
            cv2.imshow('HSV', frame)            
            time.sleep(0.01)
            #frame2 = trancking(frame, bgr)
            #cv2.imshow('BGR', frame2)            
            #frame3 = trancking(frame, gray)
            #cv2.imshow('GRAY', frame3)            
            
            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()
