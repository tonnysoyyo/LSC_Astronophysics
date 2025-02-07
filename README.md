# LSC_Astronophysics

# 📌 Colombian Sign Language (LSC, in Spanish) Recognition Project for Astronomical Concepts

## 📖 Introduction

**Colombian Sign Language (LSC)** is the natural language of the Deaf community in Colombia. It is a visual and gestural language with a unique grammatical structure, different from spoken or written Spanish. Its recognition and promotion are essential for the inclusion of deaf people in various fields, including education and scientific dissemination.

However, in the field of astronomy and space sciences, the availability of specific signs for technical terms is limited. This project seeks to address this gap by developing a **real-time sign recognition model** focused on key astronomical concepts.

---

## 🌟 Project Objective

Our main objective is to develop a system based on artificial intelligence that can recognize **10 astronomical terms** in Colombian Sign Language and translate them into text. This will facilitate access to scientific information for the deaf community and promote inclusion in education and scientific dissemination.

The terms included in this project are:

- 🌠 **Asteroid**.
- 🔭 **Astronomy**
- 💥 **Big Bang**
- ☄️ **Cometa**
- 🌒 **Ecliptic**
- 🛤️ **Celestial Equator**
- 🔥 **Meteorite**
- ✨ **Meteor**
- 🪐 **Metheoroid**
- ♒ **Zodiac**

---

## 🛠️ Tools Used

For the implementation of this project, we used a combination of advanced tools in **computer vision and artificial intelligence**:

### 📌 **MediaPipe**

[MediaPipe](https://developers.google.com/mediapipe) is a Google library specialized in **real-time image and video processing**. It allows us to detect **hands, face and body**, which is key to extract landmarks from the hands of users signing.

In this project, we use **MediaPipe Holistic**, which captures:
- 📌 **21 landmarks of each hand**.

This data is converted into numerical vectors that feed our AI model.

### 🤖 **LSTM Neural Network**.

We have implemented a **LSTM (Long Short-Term Memory)** type recurrent neural network in TensorFlow/Keras. This model is ideal for analyzing **sequences of data over time**, which is essential for gesture recognition in video.

#### 🔍 **Model features**:
- 📌 Processes **30-frame** sequences to recognize each gesture.
- 📌 Learns spatial and temporal patterns in hand movements.
- 📌 Generates a prediction with **one confidence probability** for each detected sign.

### 🎥 **OpenCV**

To capture the webcam image and process it in real time, we use [OpenCV](https://opencv.org/), a computer vision library widely used in artificial intelligence projects.

---

## 🏗️ Project Architecture

1️⃣ **Video capture:** Live image is obtained from the camera.

2️⃣ **Hand detection:** MediaPipe Holistic is used to extract hand landmarks.

3️⃣ **Sequence processing:** 30-frame sequences of key points are stored.

4️⃣ **Prediction with LSTM network:** The sequence is fed into the AI model, which predicts the realized sign.

5️⃣ **Results visualization:** The detected sign with its confidence probability is displayed on the screen.

---

## 📦 Installation and Execution

To run this project on your computer, follow these steps:

### Clone the repository
```bash
 git clone https://github.com/tonnysoyyo/LSC_Astronophysics.git
 cd LSC_Astronophysics
```

### Install dependencies
```bash
 pip install -r requirements.txt
```

### Execute real-time recognition
```bash
 python hands_process.py
```

### Execute Neural Network
```bash
 python LSTM_model.py
```

### Execute real-time test
```bash
 python real_time_test.py
```

---

## 🚀 Future of the Project.

This is just the beginning. In the future, we seek to:
- 🔹 **Expand the number of recognized signs**.
- 🔹 **Incorporate more precision in gesture recognition**.

We hope that this project will contribute to equitable access to astronomical knowledge for the deaf community. 🌌✨

---

## 📝 Credits.
This project has been developed by **[Diana Carolina Zapata and Tomas Sosa Giraldo]**, with the aim of promoting inclusion in science education and outreach. 

📫 **Contact:** 
[dianac.zapata@udea.edu.co]
[tomas.sosa@udea.edu.co]


# 📌 Proyecto de Reconocimiento de Lengua de Señas Colombiana (LSC) para Conceptos Astronómicos

## 📖 Introducción

La **Lengua de Señas Colombiana (LSC)** es el idioma natural de la comunidad sorda en Colombia. Es una lengua visual y gestual con una estructura gramatical única, diferente del español hablado o escrito. Su reconocimiento y promoción son fundamentales para la inclusión de las personas sordas en diversos ámbitos, incluyendo la educación y la divulgación científica.

Sin embargo, en el campo de la astronomía y las ciencias espaciales, la disponibilidad de señas específicas para términos técnicos es limitada. Este proyecto busca abordar esta brecha mediante el desarrollo de un **modelo de reconocimiento de señas en tiempo real**, centrado en conceptos astronómicos clave.

---

## 🌟 Objetivo del Proyecto

Nuestro objetivo principal es desarrollar un sistema basado en inteligencia artificial que permita reconocer **10 términos astronómicos** en Lengua de Señas Colombiana y los traduzca en texto. Esto facilitará el acceso a información científica para la comunidad sorda y promoverá la inclusión en el ámbito educativo y de divulgación científica.

Los términos incluidos en este proyecto son:

- 🌠 **Asteroide**
- 🔭 **Astronomía**
- 💥 **Big Bang**
- ☄️ **Cometa**
- 🌒 **Eclíptica**
- 🛤️ **Ecuador Celeste**
- 🔥 **Meteorito**
- ✨ **Meteoro**
- 🪐 **Meteoroide**
- ♒ **Zodiaco**

---

## 🛠️ Herramientas Utilizadas

Para la implementación de este proyecto, hemos utilizado una combinación de herramientas avanzadas en **visión por computadora e inteligencia artificial**:

### 📌 **MediaPipe**

[MediaPipe](https://developers.google.com/mediapipe) es una biblioteca de Google especializada en **procesamiento de imágenes y video en tiempo real**. Nos permite detectar **manos, rostro y cuerpo**, lo cual es clave para extraer los puntos de referencia (landmarks) de las manos de los usuarios que realizan señas.

En este proyecto, utilizamos **MediaPipe Holistic**, que captura:
- 📌 **21 puntos de referencia de cada mano**
- 📌 **Pose corporal (aunque solo tomamos las manos)**
- 📌 **Seguimiento en tiempo real con alta precisión**

Estos datos son convertidos en vectores numéricos que alimentan nuestro modelo de IA.

### 🤖 **Red Neuronal LSTM**

Hemos implementado una **red neuronal recurrente de tipo LSTM (Long Short-Term Memory)** en TensorFlow/Keras. Este modelo es ideal para analizar **secuencias de datos en el tiempo**, lo cual es esencial para el reconocimiento de gestos en video.

#### 🔍 **Características del modelo**:
- 📌 Procesa secuencias de **30 fotogramas** para reconocer cada seña.
- 📌 Aprende patrones espaciales y temporales en el movimiento de las manos.
- 📌 Genera una predicción con **una probabilidad de confianza** para cada seña detectada.

### 🎥 **OpenCV**

Para capturar la imagen de la webcam y procesarla en tiempo real, usamos [OpenCV](https://opencv.org/), una biblioteca de visión por computadora ampliamente utilizada en proyectos de inteligencia artificial.

---

## 🏗️ Arquitectura del Proyecto

1️⃣ **Captura de video:** Se obtiene la imagen en vivo desde la cámara.

2️⃣ **Detección de manos:** Se usa MediaPipe Holistic para extraer los puntos de referencia de las manos.

3️⃣ **Procesamiento de secuencias:** Se almacenan secuencias de 30 frames de los puntos clave.

4️⃣ **Predicción con la red LSTM:** La secuencia se introduce en el modelo de IA, que predice el signo realizado.

5️⃣ **Visualización de resultados:** Se muestra en pantalla el signo detectado con su probabilidad de confianza.

---

## 📦 Instalación y Ejecución

Para ejecutar este proyecto en tu computadora, sigue estos pasos:

### 1️⃣ Clonar el repositorio
```bash
 git clone https://github.com/tu_usuario/tu_repositorio.git
 cd tu_repositorio
```

### 2️⃣ Instalar dependencias
```bash
 pip install -r requirements.txt
```

### 3️⃣ Ejecutar el reconocimiento en tiempo real
```bash
 python reconocimiento_LSC.py
```

---

## 🚀 Futuro del Proyecto

Este es solo el inicio. En el futuro, buscamos:
- 🔹 **Ampliar el número de señas reconocidas**.
- 🔹 **Incorporar más precisión en el reconocimiento de gestos**.
- 🔹 **Optimizar el modelo para dispositivos móviles y web**.

Esperamos que este proyecto contribuya al acceso equitativo al conocimiento astronómico para la comunidad sorda. 🌌✨

---

## 📝 Créditos
Este proyecto ha sido desarrollado por **[Tu Nombre/Equipo]**, con el objetivo de impulsar la inclusión en la educación y divulgación científica. 

📫 **Contacto:** [tu.correo@example.com]

Neural Network to recognize the LSC in concepts of Astrophysics

Work in progress, based in the article: https://www.redalyc.org/journal/2570/257073797005/html/

By: Tomas Sosa Giraldo (tonnysoyyo) and Diana Carolina Zapata (dianaczapata27)