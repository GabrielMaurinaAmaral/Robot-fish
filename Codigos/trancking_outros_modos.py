import time
import cv2
import numpy as np

#? teste de rpg pra hsv depois linariza
def lineanize_black_hsv(frame):    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsv, (0, 0, 0), (255, 50, 50))   
    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
    binary_frame = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
    _,binary_frame = cv2.threshold(binary_frame, 0, 255, cv2.THRESH_BINARY)   
    cv2.imshow('binario', binary_frame) 
    return binary_frame

#! codigo rastreamento
#def trancking(frame, hsv)
#    # todo encontra pontos que circundam regiões conexas (contour)
#    contours, hierarchy = cv2.findContours(hsv, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#    #se existir contornos    
#    if contours:
#        #retornando a área do primeiro grupo de pixels brancos
#        max_Area = cv2.contourArea(contours[0])
#        contour_Max_Area_Id = 0
#        i = 0
#        #para cada grupo de pixels branco existente
#        for cnt in contours:
#            #procura o grupo com a maior área
#            if max_Area < cv2.contourArea(cnt):
#                max_Area = cv2.contourArea(cnt)
#                contour_Max_Area_Id = i
#            i += 1
#            
#        #achei o contorno com maior área em pixels
#        cntMaxArea = contours[contour_Max_Area_Id]
#        #retorna um retângulo que envolve o contorno em questão
#        x_Rect, y_Rect, w_Rect, h_Rect = cv2.boundingRect(cntMaxArea)
#        #desenha caixa envolvente com espessura 3
#        cv2.rectangle(frame, (x_Rect, y_Rect), (x_Rect + w_Rect, y_Rect + h_Rect), (0, 0, 255), 2)
#        cv2.circle(frame, (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), 5, (0, 255, 0), -1)
#        
#        #desenha o ponto no meio da camera
#        height, width, _ = frame.shape
#
#        cv2.circle(frame, (int(width/2), int(height/2)), 5, (255, 0, 0), -1)
#        #desenha o vetor do ponto centra da tela a ate o ponto central da regiao detectada        
#        frame = cv2.line(frame, (int(width/2), int(height/2)), (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), (0, 255, 0), 2)
#    return frame
    
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
        # parametro pra aproximar os cortonos
        epsilon = 0.001 * cv2.arcLength(cntMaxArea, True)
        aprox = cv2.approxPolyDP(cntMaxArea, epsilon, True)
        # Exiba a imagem com contorno 
        frame_1 = frame
        cv2.drawContours(frame_1, [aprox], -1, (255, 0, 255), 2)
        cv2.imshow('contor fixo', frame_1) 
        # caixa de acordo com o cortorno para minimo possivel
        frame_2 = frame        
        rect = cv2.minAreaRect(cntMaxArea)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame_2,[box],0,(0,255,255),2)
        cv2.imshow('contor', frame_2) 
        # orientação é o ângulo em que o objeto é direcionado
        (x,y),(MA,ma),angle = cv2.fitEllipse (cntMaxArea)
        print(f"x:{int(x)}\ny:{int(y)}\nMA:{int(MA)}\nma:{int(ma)}\nangle:{int(angle)}",)
        #retorna um retângulo que envolve o contorno em questão
        x_Rect, y_Rect, w_Rect, h_Rect = cv2.boundingRect(cntMaxArea)
        #desenha caixa envolvente com espessura 3
        cv2.rectangle(frame, (x_Rect, y_Rect), (x_Rect + w_Rect, y_Rect + h_Rect), (0, 0, 255), 2)
        cv2.circle(frame, (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), 5, (0, 255, 0), -1)
        #*desenha o ponto no meio da camera
        height, width, _ = frame.shape
        cv2.circle(frame, (int(width/2), int(height/2)), 5, (255, 100, 0), -1)
        #//desenha o vetor do ponto centra da tela a ate o ponto central da regiao detectada        
        frame = cv2.line(frame, (int(width/2), int(height/2)), (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), (0, 255, 0), 2)
    return frame    
    
def main():
    webcam = cv2.VideoCapture(0)
    
    while True:
        validacao, frame = webcam.read()
    
        if validacao:           
            
            hsv = lineanize_black_hsv(frame)

            frame = trancking(frame, hsv)
            cv2.imshow('HSV', frame)            
            time.sleep(0.01)

            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()
