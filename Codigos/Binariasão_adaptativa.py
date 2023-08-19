import time
import cv2
import numpy as np

# binarização sem adaptação
#def lineanize_hsv(frame):      
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    cv2.imshow('HSV', hsv)
#    
#    black_mask = cv2.inRange(hsv, (0, 0, 0), (255, 50, 50))
#    cv2.imshow('intervalo só preto', black_mask)
#    
#    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
#    cv2.imshow('pos mascara', black_result)
#
#    frame = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('pos mascara CINZA', frame)
#    
#    _,frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)  
#    cv2.imshow('HSV binario', frame)
#    
#    kernel = np.ones((2, 2), np.uint8)
#    frame = cv2.dilate(frame, kernel, iterations=1)
#    cv2.imshow('com menos ruido', frame)
#
#    return frame
    
def lineanize_hsv_adaptado(frame):      
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsv, (0, 0, 0), (255, 50, 50))
    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
    frame = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Binario', frame)
    
    # dois ultimos parametros que ajustão
    # O valor limite é a média da área da vizinhança menos a constante 
    # frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,0)
    # O valor limite é uma soma ponderada gaussiana dos valores da vizinhança menos a constante C
    frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,0)
    cv2.imshow('binario adapatado', frame)
    
    # Otsu determina um valor limite global ideal a partir do histograma da imagem.
    _, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('binario + otsu', frame)
    
    #kernel = np.ones((4, 4), np.uint8)
    # Kernel em forma de cruz
    kernel =cv2.getStructuringElement (cv2.MORPH_CROSS,(5,5))
        
    #preenchimento por dilatação de pixel
    frame = cv2.dilate(frame, kernel, iterations=2)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('binario com menos ruido', frame)

    return frame    
    
def trancking(frame, hsv):
    contours, hierarchy = cv2.findContours(hsv, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_Area = cv2.contourArea(contours[0])
        contour_Max_Area_Id = 0
        i = 0
        for cnt in contours:
            if max_Area < cv2.contourArea(cnt):
                max_Area = cv2.contourArea(cnt)
                contour_Max_Area_Id = i
            i += 1
            
        cntMaxArea = contours[contour_Max_Area_Id]
        x_Rect, y_Rect, w_Rect, h_Rect = cv2.boundingRect(cntMaxArea)
        
        cv2.rectangle(frame, (x_Rect, y_Rect), (x_Rect + w_Rect, y_Rect + h_Rect), (0, 0, 255), 2)
        cv2.circle(frame, (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), 5, (0, 255, 0), -1)        
        
        height, width, _ = frame.shape
        cv2.circle(frame, (int(width/2), int(height/2)), 5, (255, 0, 0), -1)
        
        frame = cv2.line(frame, (int(width/2), int(height/2)), (x_Rect + int(w_Rect/2), y_Rect + int(h_Rect/2)), (0, 255, 0), 2)
        
        vetor_AB = np.array([x_Rect + int(w_Rect/2) - int(width/2), y_Rect + int(h_Rect/2) - int(height/2)])
        
        escalar_AB = np.linalg.norm(vetor_AB)     
        print("\nVetor AB:", vetor_AB)
        print("Escalar AB:", int(escalar_AB))

    return frame
    
def main():
    webcam = cv2.VideoCapture(0)
    
    while True:
        validacao, frame = webcam.read()
    
        if validacao:           
            ini = cv2.getTickCount ()

            hsv = lineanize_hsv_adaptado(frame)
            frame = trancking(frame, hsv)
            
            fim = cv2.getTickCount ()
            tempo = (fim - ini)/ cv2.getTickFrequency ()
            print('tempo de execução', tempo)
            
            cv2.imshow('HSV', frame)            
            time.sleep(0.1)

            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()