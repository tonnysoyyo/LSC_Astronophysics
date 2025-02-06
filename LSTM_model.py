import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
from hands_process import actions
from utils.img_helper import load_data
from utils.ML_helper import build_model
from constants import DATA_PATH, no_sequences, sequence_length

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

label_map = {label:num for num, label in enumerate(actions)}

sequences, labels = load_data(DATA_PATH, actions, no_sequences, sequence_length, label_map)

X = np.array(sequences)
y = to_categorical(labels).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = build_model(actions)

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

early_stop = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
model.fit(X_train, y_train, epochs=2000, batch_size=32, validation_split=0.2, callbacks=[tb_callback, early_stop])