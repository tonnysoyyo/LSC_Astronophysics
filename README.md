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