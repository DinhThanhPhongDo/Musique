import matplotlib
from scipy.io import wavfile
from matplotlib import pyplot as plt
import constant as cst
import numpy as np
#samplerate, data = wavfile.read('./output/audio.wav')


#samplerate =44100, #frequence d'echantillonage [1/s]
#samplerate = 44100; fs = 100#
#t = np.linspace(0., 1., samplerate)
#amplitude = np.iinfo(np.int16).max
#data = amplitude * np.sin(2. * np.pi * fs * t)
#wavfile.write("example.wav", samplerate, data.astype(np.int16))


class MySong():
    #static variable:
    
    def __init__(self):

        self.notes  = []
        self.rythms = []
        self.wave   = []
        self.duration = 0.
        self.tempo  = -1
        self.fs     = -1
        self.A      = lambda t: np.iinfo(np.int16).max
    
    def set_tempo(self,tempo):
        self.tempo = tempo
    
    def set_fs(self,fs):
        self.fs =fs

    def set_A(self, A):
        self.A = A

    def add_note(self,note,rythm):
        self.notes.append(note)
        self.rythms.append(rythm)
    
    def add_notes(self,notes,rythms):
        self.notes.extend(notes)
        self.rythms.extend(rythms)
        self.duration += np.sum(rythms)* 60/self.tempo 
    
    def add_chord(self,chord,rythm):

        self.notes.append(chord)
        self.notes.append(rythm)

    def add_chords(self,chords, rythms):
        self.notes.extend(chords)
        self.notes.extend(rythms)

    def MakeSong(self,filename):

        T = 60/self.tempo
        for note,rythm in zip(self.notes,self.rythms):
            freq = cst.NOTES[note]
            self.wave.extend([self.A(t)*np.sin(2. * np.pi * freq * (t/self.fs)) for t in range(int(self.fs*T*rythm))])
            print(note)
        wave =np.array(self.wave)
        wavfile.write(filename, self.fs, wave.astype(np.int16))
    
    def plot(self):
        x = np.linspace(0,self.duration,len(self.wave))
        plt.plot(x,self.wave)
        plt.show()


song  = MySong()
song.set_tempo(180)
song.set_fs(44100)
song.add_notes(["e5","e5","s","e5","s","c5","e5","g5","s","g4"],
               [0.5 ,0.5 ,0.5,0.5 ,0.5,0.5 ,1.  ,1.  ,1. ,1.])
song.add_notes(["c5","s","g4","s","e4","s","a4","b4","b4-","a4","g4","e5","g5","a5","f5","g5","s","e5","c5","d5","b4","s"],
               [1.  ,0.5,0.5  ,0.5,0.5,0.5,1.  ,1.  ,0.5  ,1.  ,0.33,0.33,0.33,1.  , 0.5, 0.5,0.5, 1. ,0.5 ,0.5 , 1.  ,0.5])
song.add_notes(["c5","s","g4","s","e4","s","a4","b4","b4-","a4","g4","e5","g5","a5","f5","g5","s","e5","c5","d5","b4","s"],
               [1.  ,0.5,0.5  ,0.5,0.5,0.5,1.  ,1.  ,0.5  ,1.  ,0.33,0.33,0.33,1.  , 0.5, 0.5,0.5, 1. ,0.5 ,0.5 , 1.  ,0.5])

song.add_notes(["s","g5","f5+","f5","d5+","e5","s","g4+","a4","c5","s","a4","c5","d5","s","g5","f5+","f5","d5+","e5","s","c6","c6","c6","s"],
               [1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,0.5  , 0.5,0.5 , 0.5,0.5,0.5 , 0.5,1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,1.  ,0.5 , 1.,1.])
song.add_notes(["s","g5","f5+","f5","d5+","e5","s","g4+","a4","c5","s","a4","c5","d5","s","e5-","d5","c5","s","g3","g3","c3"],
               [1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,0.5  , 0.5,0.5 , 0.5,0.5,0.5 , 0.5,1. ,1.   ,1.  ,1. ,0.5,0.5 ,1.  ,1. ])
song.add_notes(["s","g5","f5+","f5","d5+","e5","s","g4+","a4","c5","s","a4","c5","d5","s","g5","f5+","f5","d5+","e5","s","c6","c6","c6","s"],
               [1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,0.5  , 0.5,0.5 , 0.5,0.5,0.5 , 0.5,1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,1.  ,0.5 , 1.,1.])
song.add_notes(["s","g5","f5+","f5","d5+","e5","s","g4+","a4","c5","s","a4","c5","d5","s","e5-","d5","c5","s","g3","g3","c3"],
               [1. , 0.5,0.5  ,0.5 , 1.  , 0.5,0.5,0.5  , 0.5,0.5 , 0.5,0.5,0.5 , 0.5,1. ,1.   ,1.  ,1. ,0.5,0.5 ,1.  ,1. ])
song.MakeSong("mario.wav")
song.plot()