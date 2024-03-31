import numpy as np
import matplotlib.pyplot as plt
import librosa
import pandas as pd

one, sr = librosa.load("C:/Users/tvtha/Desktop/1test.wav")
two, sr = librosa.load("C:/Users/tvtha/Desktop/2test.wav")
three, sr = librosa.load("C:/Users/tvtha/Desktop/3test.wav")
four, sr = librosa.load("C:/Users/tvtha/Desktop/4test.wav")
five, sr = librosa.load("C:/Users/tvtha/Desktop/5test.wav")
six, sr = librosa.load("C:/Users/tvtha/Desktop/6test.wav")
#seven is the input file
seven, sr = librosa.load("C:/Users/tvtha/Desktop/7test.wav")

min_length = min(len(one), len(two), len(three),len(four),len(five),len(six),len(seven))
one = one[:min_length]
two = two[:min_length]
three = three[:min_length]
four = four[:min_length]
five = five[:min_length]
six = six[:min_length]
seven = seven[:min_length]

c_add = one + two + three
t_add = four + five + six

def pms(signal, title, sr,f_ratio = 1):  
    ft = np.fft.fft(signal)
    ms = np.abs(ft)
    plt.figure(figsize = (18,5))
    frequency = np.linspace(0,sr,len(ms))
    num_frequency_bins = int(len(frequency)*f_ratio)

    plt.plot(frequency[:num_frequency_bins],ms[:num_frequency_bins])
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.title(title)

c_wave = pms(c_add,"Coimbatore Tamil",sr,0.1)
t_wave = pms(t_add,"Tirunelveli Tamil",sr,0.1)
i_wave = pms(seven,"Given Input",sr,0.1)

c_series = pd.Series(c_wave)
t_series = pd.Series(t_wave)
i_series = pd.Series(i_wave)

correlation1 = c_series.corr(i_series)
correlation2 = t_series.corr(i_series)

if (correlation1 > correlation2):
    print("Coimbatore Tamil")
elif (correlation2 > correlation1):
    print("Tirunelveli Tamil")    

plt.show()
