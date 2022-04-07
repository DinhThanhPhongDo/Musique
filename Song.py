from scipy.io import wavfile
import notes as *
import numpy as np
samplerate, data = wavfile.read('./output/audio.wav')


samplerate =44100, #frequence d'echantillonage [1/s]
samplerate = 44100; fs = 100
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
wavfile.write("example.wav", samplerate, data.astype(np.int16))


class MySong():
    #static variable:
    
    def __init__(self):

        self.notes = []
        self.rythms = []
        self.tempo = 0
    
    def add_note(self,note,rythm):
        self.notes.append(note)
        self.rythms.append(rythm)
    
    def add_notes(self,notes,rythms):
        self.notes.extend(notes)
        self.notes.extend(rythms)
    
    def add_chord(self,chord,rythm):

        self.notes.append(chord)
        self.notes.append(rythm)

    def add_chords(self,chords, rythms):
        self.notes.extend(chords)
        self.notes.extend(rythms)