from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_model(actions):
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 126)))
    model.add(Dropout(0.4))  # Increased dropout

    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dropout(0.4))

    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(actions), activation='softmax'))
    return model