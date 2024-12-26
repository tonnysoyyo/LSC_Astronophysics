# import mediapipe as mp
# import os
# import cv2

# # Inicializar MediaPipe Hands
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# # Crear directorios para almacenar las imágenes
# clases = ['test1', 'test2', 'test3']  # Reemplazar con las palabras o señas específicas
# ruta_base = "Dataset/Test_processed"
# os.makedirs(ruta_base, exist_ok=True)
# for clase in clases:
#     os.makedirs(os.path.join(ruta_base, clase), exist_ok=True)

# # Ruta de la carpeta con los videos
# ruta_videos = "Dataset/Test"
# archivos_videos = [os.path.join(ruta_videos, f) for f in os.listdir(ruta_videos) if f.endswith('.mp4') or f.endswith('.avi')]

# # Procesar cada video de la carpeta
# for video_path in archivos_videos:
#     cap = cv2.VideoCapture(video_path)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Procesar el cuadro para detectar manos
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         result = hands.process(rgb_frame)

#         if result.multi_hand_landmarks:
#             for hand_landmarks in result.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#                 # Extraer los puntos de interés y recortar la imagen
#                 h, w, _ = frame.shape
#                 x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
#                 x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
#                 y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
#                 y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)
#                 recorte = frame[y_min:y_max, x_min:x_max]

#                 # Redimensionar la imagen y almacenarla
#                 if recorte.size > 0:
#                     recorte = cv2.resize(recorte, (200, 200))
#                     # etiqueta = "clase1"  # Cambiar dinámicamente según la clase
#                     # cv2.imwrite(os.path.join(ruta_base, etiqueta, f"{etiqueta}_{len(os.listdir(os.path.join(ruta_base, etiqueta)))}.jpg"), recorte)
#                     # Dynamically determine the class (etiqueta) based on video name
#                     etiqueta = os.path.basename(video_path).split('.')[0]  # Example: Use video name as label
#                     if etiqueta not in clases:
#                         print(f"Skipping video {video_path}, no matching class directory found.")
#                         continue

#                     # Ensure the directory exists before saving
#                     save_path = os.path.join(ruta_base, etiqueta)
#                     os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
#                     cv2.imwrite(os.path.join(save_path, f"{etiqueta}_{len(os.listdir(save_path))}.jpg"), recorte)

#         cv2.imshow('Procesando Video', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()

# cv2.destroyAllWindows()


import mediapipe as mp
import os
import cv2

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Crear directorios para almacenar las imágenes
clases = ['test1', 'test2', 'test3']  # Reemplazar con las palabras o señas específicas
ruta_base = "Dataset/Test_processed"
os.makedirs(ruta_base, exist_ok=True)
for clase in clases:
    os.makedirs(os.path.join(ruta_base, clase), exist_ok=True)

# Ruta de la carpeta con los videos
ruta_videos = "Dataset/Test"
archivos_videos = [os.path.join(ruta_videos, f) for f in os.listdir(ruta_videos) if f.endswith('.mp4') or f.endswith('.avi')]

# Procesar cada video de la carpeta
for video_path in archivos_videos:
    cap = cv2.VideoCapture(video_path)
    
    # Obtener propiedades del video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Preparar el VideoWriter para guardar el video procesado
    video_name = os.path.basename(video_path).split('.')[0]
    output_path = os.path.join(ruta_base, f"{video_name}_processed.mp4")
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Procesar el cuadro para detectar manos
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraer los puntos de interés y recortar la imagen
                h, w, _ = frame.shape
                x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
                x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
                y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
                y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)
                recorte = frame[y_min:y_max, x_min:x_max]

                # Redimensionar la imagen y almacenarla
                if recorte.size > 0:
                    recorte = cv2.resize(recorte, (200, 200))
                    etiqueta = os.path.basename(video_path).split('.')[0]  # Example: Use video name as label
                    if etiqueta not in clases:
                        print(f"Skipping video {video_path}, no matching class directory found.")
                        continue

                    # Ensure the directory exists before saving
                    save_path = os.path.join(ruta_base, etiqueta)
                    os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
                    cv2.imwrite(os.path.join(save_path, f"{etiqueta}_{len(os.listdir(save_path))}.jpg"), recorte)

        # Escribir el cuadro procesado en el video de salida
        out.write(frame)

        cv2.imshow('Procesando Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

cv2.destroyAllWindows()
