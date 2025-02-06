import os
import numpy as np
from utils.img_helper import create_dir, take_data
from constants import DATA_PATH, no_sequences, sequence_length

# Actions that we try to detect
actions = np.array(['Asteroide', 'Astronomia', 'Big_bang', 'Cometa', 'Ecliptica', 'Ecuador_celeste', 
                    'Meteorito', 'Meteoro', 'Meteoroide', 'Zodiaco'])

create_dir(DATA_PATH, actions, no_sequences)

take_data(DATA_PATH, actions, no_sequences, sequence_length)
