import cv2

cap = cv2.VideoCapture(0)  # Use o índice da câmera padrão ou ajuste conforme necessário

# Verifique se a câmera foi aberta com sucesso
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
else:
    while True:
        # Capture um quadro da câmera
        ret, frame = cap.read()

        # Verifique se o quadro foi capturado com sucesso
        if not ret:
            print("Erro ao capturar o quadro.")
            break

        # Determine as coordenadas da região que você deseja capturar
        x = 100  # Coordenada x do canto superior esquerdo
        y = 100  # Coordenada y do canto superior esquerdo
        width = 400  # Largura da região
        height = 300  # Altura da região

        # Recorte a região de interesse
        cropped_frame = frame[y:y+height, x:x+width]

        # Exiba a região recortada
        cv2.imshow("Câmera", cropped_frame)

        # Aguarde um pouco e verifique se o usuário pressionou a tecla 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libere a câmera e feche a janela
    cap.release()
    cv2.destroyAllWindows()
