#! /usr/bin/env python3

import numpy as np
from scipy.io import wavfile
from baudot_code import letter, figure

def baudot_generator(message):
    audio_file_name = ''
    sample_rate = 8000
    space_frequency = 2295
    mark_frequency = 2125
    mr = 50
    length = 1 / mr
    letter_number = 1
    data = '11111 11111 11111 11111 11111'

    #########################
    ##  Message to Binary  ##
    #########################
    for character in message:
        if character == ' ':
            character = '~'

        # LETTER or FIGURE designation
        elif character == '@':
            letter_number = 1
            data += '0111111'
        elif character == '*':
            letter_number == 2
            data += '0110111'

        # LETTER or FIGURE added to data stream
        if letter_number == 1:
            for key in letter.keys():
                if character == key:
                    data += letter[key]
        elif letter_number == 2:
            for key in figure.keys():
                if character == key:
                    data += figure[key]

    #############################
    ##  Audio File Production  ##
    #############################
    data_array = []
    time = np.linspace(0, length, sample_rate * length)
    for sample in range(len(data)):
        if data[sample] == '0':
            sin_wave = np.sin(space_frequency * 2 * np.pi * time)
        elif data[sample] == '1':
            sin_wave = np.sin(mark_frequency * 2 * np.py * time)
        data_array = np.concatenate((data_array, sin_wave))
    numpy_data = np.array(data_array, dtype=float)
    wavfile.write(audio_file_name, sample_rate, numpy_data)


if __name__ == '__main__':
    #    > == null, < == cr, [ == lf, % == BELL
    baudot_generator('@ryryry the quick brown fox jumps over the lazy dog<[*0123456789 (-.-;)<[@')
