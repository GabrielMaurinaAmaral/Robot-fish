import time
import cv2
import numpy as np


def lineanize_black_hsv(frame):      
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsv, (0, 20, 0), (255, 255, 90))
    black_result= cv2.bitwise_and(frame, frame, mask=black_mask)
    
    binary_frame = cv2.cvtColor( black_result, cv2.COLOR_BGR2GRAY)
    _,binary_frame = cv2.threshold(binary_frame, 0, 255, cv2.THRESH_BINARY)   
    cv2.imshow('Imagem binaria por hsv', binary_frame)
    
    pixel_cover = np.ones((2, 2), np.uint8)
    binary_frame = cv2.dilate(binary_frame, pixel_cover, iterations=6)
    cv2.imshow('Imagem com menos ruido', binary_frame)

    return binary_frame
    
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
            
            hsv = lineanize_black_hsv(frame)

            frame = trancking(frame, hsv)
            cv2.imshow('HSV', frame)            
            time.sleep(1)

            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()
