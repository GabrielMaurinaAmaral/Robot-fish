import cv2

# nicialize a câmera (0 representa a câmera padrão, geralmente a webcam embutida)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
# Verifique se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

while True:
    # Capture um quadro da câmera
    ret, frame = cap.read()

    # Verifique se a captura foi bem-sucedida
    if not ret:
        print("Erro ao capturar o quadro.")
        break

    # Exiba o quadro capturado em uma janela
    cv2.imshow('Camera Test', frame)

    # Aguarde por uma tecla (pressione 'q' para sair)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a câmera e feche todas as janelas
cap.release()
cv2.destroyAllWindows()
