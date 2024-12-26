from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import TensorBoard
import tensorflow as tf
from utils.ML_helper import cargar_datos_y_etiquetas

clases = []  # TODO: Fill in the classes (check if it's okay)

# Upload the dataset
imagenes, etiquetas = cargar_datos_y_etiquetas()
x_train, x_test, y_train, y_test = train_test_split(imagenes, etiquetas, test_size=0.2, random_state=42)

# Convolutional Neural Network (CNN)
modelo = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(256, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(clases), activation='softmax')
])

modelo.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
tensorboard = TensorBoard(log_dir="logs")
modelo.fit(x_train, y_train, epochs=30, batch_size=32, validation_data=(x_test, y_test), callbacks=[tensorboard])

# Evaluation and metrics
resultados = modelo.evaluate(x_test, y_test)
print(f"Precisión: {resultados[1] * 100:.2f}%")

# Save the model
modelo.save('modelo_lsc.h5')