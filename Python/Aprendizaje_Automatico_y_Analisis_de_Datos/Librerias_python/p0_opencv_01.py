import cv2
import numpy as np

# Crear una imagen negra de 400x200 píxeles
imagen = np.zeros((200, 400, 3), dtype=np.uint8)

# Escribir el texto "Hola Mundo" en la imagen
cv2.putText(imagen, 'Hola Mundo', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

# Mostrar la imagen en una ventana llamada "Hola Mundo"
cv2.imshow('Hola Mundo', imagen)

# Esperar hasta que se presione cualquier tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
