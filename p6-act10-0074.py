import numpy as np 
import cv2 # Vision artificial act10 NC 0074 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# lee la imagen en escala de grises 
img = cv2.imread('Tierra.jpg', cv2.IMREAD_GRAYSCALE) 

# NOTA: imread no lanza error si no encuentra el archivo, solo devuelve None.
# Revisamos antes de seguir para que el mensaje sea claro.
if img is None:
    raise FileNotFoundError("No se encontró 'Tierra.jpg'. Revisa que esté en la misma carpeta que el script.")

# Abre la ventana con la imagen 
cv2.imshow('El planeta 0074', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Linea 
print('La Linea 0074') 

# NOTA: una imagen en escala de grises tiene un solo canal, así que el color
# (255,0,0) se vería blanco en vez de azul. La pasamos a BGR (3 canales,
# aunque se vea igual de gris) para poder dibujar en color.
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# NOTA: en vez de usar un número fijo, calculamos el centro real de la imagen.
alto, ancho = img.shape[:2]
centro = (ancho // 2, alto // 2)

# AQUI CREA EL CIRCULO 
# Dibuja un circulo azul de radio 10px al centro de la imagen 
img = cv2.circle(img, centro, 10, (255,0,0), -1) 

# TEXTO 
# Añade a la imagen el texto Example Text en color blanco 
img = cv2.putText(img, 'Vision artificial 0074', (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2) 

# NOTA: en el original nunca se mostraba el resultado, así que no se veía nada.
cv2.imshow('Circulo y texto', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crea una imagen negra 
img = np.zeros((512,512,3), np.uint8) 

# Dibuja una diagonal blanca de 3px desde una esquina a la otra 
img = cv2.line(img, (0,0), (511,511), (255,255,255), 3) 

# Dibuja un circulo azul de radio 10px al centro de la imagen 
# NOTA: el centro de una imagen de 512x512 es (256,256), no (260,260).
img = cv2.circle(img, (256,256), 10, (255,0,0), -1) 

# NOTA: igual que arriba, mostramos la imagen para ver la diagonal y el círculo.
cv2.imshow('Linea y circulo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aqui empieza el trackbar 
def on_trackbar(val): 
    # NOTA: aquí solo imprimimos el valor; el color real se lee dentro del ciclo.
    print(val) 

# Crea a una imagen negra, y una ventana llamada frame 
img = np.zeros((300,512,3), np.uint8) 
cv2.namedWindow('frame') 

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar() 
cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar) 
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar) 
cv2.createTrackbar('B', 'frame', 0, 255, on_trackbar) 

while(True): 
    cv2.imshow('frame', img) 
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:  # tecla ESC para salir
        break 

    # Obtiene las posiciones de los trackbars 
    # NOTA: si la ventana se cerró con la X, getTrackbarPos lanza cv2.error;
    # lo atrapamos y salimos del ciclo.
    try:
        r = cv2.getTrackbarPos('R', 'frame') 
        g = cv2.getTrackbarPos('G', 'frame') 
        b = cv2.getTrackbarPos('B', 'frame') 
    except cv2.error:
        break

    # NOTA: OpenCV usa el orden B, G, R (no R, G, B), por eso van así.
    img[:] = [b, g, r] 

cv2.destroyAllWindows() 

# NOTA: se usa Tierra.jpg porque Tierra.png no existe en la carpeta.
img = cv2.imread('Tierra.jpg', 0) 

# NOTA: misma validación de antes; sin esto, threshold marca un error confuso.
if img is None:
    raise FileNotFoundError("No se encontró 'Tierra.jpg'. Revisa que esté en la misma carpeta que el script.")

# NOTA: todos usan umbral 127 y valor máximo 255; solo cambia el tipo de umbralizado.
ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) 
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) 
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) 

cv2.imshow('BINARY', thr1) 
cv2.imshow('BINARY_INV', thr2) 
cv2.imshow('TRUNC', thr3) 
cv2.imshow('TOZERO', thr4) 
cv2.imshow('TOZERO_INV', thr5) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 

print('JAQUEZ CAMACHO JOEL ANDRES 0074')