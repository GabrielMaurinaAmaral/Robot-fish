import cv2
import numpy as np

def detect_plate(frame, lower_plate_color, upper_plate_color):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    plate_mask = cv2.inRange(hsv_frame, lower_plate_color, upper_plate_color)
    plate_result = cv2.bitwise_and(frame, frame, mask=plate_mask)
    return plate_result

def main():
    webcam = cv2.VideoCapture(0)
    
    # Defina os intervalos de cor para o prato (ajuste conforme necessário)
    lower_plate_color = np.array([H_MIN, S_MIN, V_MIN])
    upper_plate_color = np.array([H_MAX, S_MAX, V_MAX])
    
    while True:
        validacao, frame = webcam.read()
    
        if validacao:
            plate_detected = detect_plate(frame, lower_plate_color, upper_plate_color)
            
            cv2.imshow('Plate Detection', plate_detected)
            
            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
