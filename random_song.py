import numpy as np
import random

class Random_song():
    def __init__(self, tracks = [], tempo = 400, measures = 4, beats_per_measure = 16, normalization_factor = 0.5):
        self.tempo = tempo
        self.measures = measures
        self.beats_per_measure = beats_per_measure
        self.beats = beats_per_measure * measures
        self.normalization_factor = 0.5
        self.chord_list = ["C", "D", "E", "F", "G", "A", "B"]
        self.lockdown = [None] * measures
        self.key_change = self.generate_key_change()
        self.tracks = tracks

    def preset_1(self):
        self.lockdown = ["A", None, None, None] * (self.measures/4)
        self.key_change = self.generate_key_change()
        self.add_track(o = 2, track_type = "bass", smdif = 4, emptiness = 0.6)
        self.add_track(o = 4, track_type = "chordal", smdif = 2, emptiness = 0.5)
        self.add_track(o = 3, track_type = "chordal", smdif = 2, emptiness = 0.7)
        self.add_track(o = 5, track_type = "melodic", smdif = 1, emptiness = 0.6)
        self.add_track(o = 2, track_type = "bass", smdif = 1, emptiness = 0.6)
        self.tempo = 400

    def preset_2(self):
        self.lockdown = ["C", "B", "A", "G"] * (self.measures/4)
        self.key_change = self.generate_key_change()
        self.add_track(o = 2, track_type = "bass", smdif = 8, emptiness = 0.0)
        self.add_track(o = 3, track_type = "chordal", smdif = 4, emptiness = 0.7)
        self.add_track(o = 4, track_type = "melodic", smdif = 2, emptiness = 0.4)
        self.add_track(o = 5, track_type = "melodic", smdif = 4, emptiness = 0.3)
        self.tempo = 420

    def record(self):
        song_file = open("last_song.txt", "w")
        song_file.write(str(np.concatenate(self.tracks, 1)))
        song_file.close

    def generate_key_change(self):
        key_change = [["."] * self.measures]
        for i in range(0, self.measures):
            chord = random.choice(self.chord_list)
            key_change[0][i] = chord
            if i > 0:
                while chord == key_change[0][i - 1]:
                    chord = random.choice(self.chord_list)
                    key_change[0][i] = chord
            index = 0
        for item in self.lockdown:
            if item != None:
                key_change[0][index] = self.lockdown[index]
            index += 1
        print(self.lockdown, key_change)
        return np.asarray(key_change).T

    def add_track(self, emptiness = None, smdif = None, rhclone = None,
                  rhdodge = None, track_type = None, o = None):
        if not smdif:
            smdif = random.choice([1, 2, 4, 8])
        if not track_type:
            track_type = random.choice(["bass", "melodic", "chordal"])
        if not o:
            o = random.choice([2, 3, 4, 5])
        if not emptiness:
            emptiness = random.random() * (1 - self.normalization_factor) + 0.5 * (self.normalization_factor)
        print(emptiness)
        track = Random_track(emptiness = emptiness,
                             smdif = smdif,
                             key_change = self.key_change,
                             beats_per_measure = self.beats_per_measure,
                             rhclone = rhclone,
                             rhdodge = rhdodge,
                             track_type = track_type,
                             o = o)
        self.tracks.append(track.get_track())

    def get_tracks(self):
        return self.tracks

    def silence(num_beats):
        rests = ". " * num_beats
        return np.asarray([rests.split()]).T

class Random_track():
    def __init__(self, emptiness = random.random(), key_change = [], beats_per_measure = 16, smdif = 4, rhclone = None, rhdodge = None, track_type = "melodic", o = 4):
        # rhclone is a track to clone the rhythm of. rhdodge is a track to
        # specifically avoid the rhythm of. smdif is the smallist differentiable
        # rhythm --- r, at a bpm of 16, would be a quarter note.
        o1 = str(o + 1)
        o = str(o)

        bass_dict = {"C" : ["C"+o, "G"+o],
                    "D" : ["D"+o, "A"+o],
                    "E" : ["E"+o, "B"+o],
                    "F" : ["F"+o, "C"+o],
                    "G" : ["G"+o, "D"+o],
                    "A" : ["A"+o, "E"+o],
                    "B" : ["B"+o, "G"+o]}

        key_dict = {"C" : ["C"+o, "D"+o, "E"+o, "G"+o],
                    "D" : ["E"+o, "F"+o, "C"+o, "D"+o, "A"+o],
                    "E" : ["G"+o, "B"+o, "D"+o, "E"+o],
                    "F" : ["F"+o, "G"+o, "A"+o, "C"+o],
                    "G" : ["G"+o, "B"+o, "D"+o, "A"+o],
                    "A" : ["A"+o, "B"+o, "C"+o, "E"+o, "G"+o],
                    "B" : ["B"+o, "D"+o, "G"+o, "A"+o]}

        arpeggio_dict =  {"C" : ["C"+o, "E"+o, "G"+o, "C"+o1],
                          "D" : ["F"+o, "A"+o, "D"+o, "D"+o1],
                          "E" : ["G"+o, "B"+o, "E"+o, "E"+o1],
                          "F" : ["F"+o, "A"+o, "C"+o, "F"+o1],
                          "G" : ["G"+o, "B"+o, "D"+o, "G"+o1],
                          "A" : ["A"+o, "C"+o, "E"+o, "A"+o1],
                          "B" : ["B"+o, "D"+o, "G"+o]}

        notes_dict = {"bass" : bass_dict, "melodic" : key_dict, "chordal" : arpeggio_dict}
        notes = notes_dict[track_type]
        beats = beats_per_measure * len(key_change)
        track = [["."] * beats]
        smdif = 16/smdif

        for i in range(0, beats):
            if i%(beats_per_measure/smdif) == 0 and random.random() > emptiness:
                track[0][i] = random.choice(notes[key_change[i/beats_per_measure, 0]])
            if track_type == "chordal" and i%(beats_per_measure) == 0:
                track[0][i] = random.choice(notes[key_change[i/beats_per_measure, 0]])
            if track_type == "bass" and i%(beats_per_measure) == 0:
                track[0][i] = key_change[i/beats_per_measure, 0] + o
        self.track = np.asarray(track).T

    def get_track(self):
        return self.track

"""
        bass_emptiness = random.random() * (1-self.normalization_factor) + 0.5 * self.normalization_factor
        chord_emptiness = random.random() * (1-normalization_factor) + 0.5 * normalization_factor
        crazybass_emptiness = random.random() * (1-normalization_factor) + 0.5 * normalization_factor
        melody_emptiness = random.random() * (1-normalization_factor) + 0.5 * normalization_factor
        countermelody_emptiness = random.random() * (1-normalization_factor) + 0.5 * normalization_factor
        emptiness = (0, bass_emptiness, chord_emptiness, crazybass_emptiness, melody_emptiness, countermelody_emptiness)
        track_0 = silence(beats)
        chord_list = ["C2", "D2", "E2", "F2", "G2", "A2", "B2"]

        bass_dict = {"C2" : ["C2", "G2"],
                    "D2" : ["D2", "A2"],
                    "E2" : ["E2", "B2"],
                    "F2" : ["F2", "C2"],
                    "G2" : ["G2", "D2"],
                    "A2" : ["A2", "E2"],
                    "B2" : ["B2", "G2"]}

        key_dict = {"C2" : ["C5", "D5", "E5", "G5", "B5"],
                    "D2" : ["E5", "F5", "C5", "D5", "A5"],
                    "E2" : ["G5", "B5", "D5", "E5"],
                    "F2" : ["F5", "G5", "A5", "C5", "E5"],
                    "G2" : ["G5", "B5", "D5", "F5", "A5"],
                    "A2" : ["A5", "B5", "C5", "E5", "G5"],
                    "B2" : ["B5", "D5", "G5", "A5"]}

        arpeggio_dict =  {"C2" : ["C4", "E4", "G4"],
                          "D2" : ["F4", "A4", "D4"],
                          "E2" : ["G4", "B4", "E4"],
                          "F2" : ["F4", "A4", "C4"],
                          "G2" : ["G4", "B4", "D4"],
                          "A2" : ["A4", "C4", "E4"],
                          "B2" : ["B4", "D4", "G4"]}

        chord_change = [["."] * measures]
        for i in range(0, measures):
            chord = random.choice(chord_list)
            chord_change[0][i] = chord
            if i > 0:
                while chord == chord_change[0][i - 1]:
                    chord = random.choice(chord_list)
                    chord_change[0][i] = chord
                    print("stuck")
            else:
                pass
                #chord_change[0][i] = "A2"
        chord_change = np.asarray(chord_change).T

        bassline = [["."] * beats]
        for i in range(0, beats):
            if i%(beats_per_measure/4) == 0:
                bassline[0][i] = chord_change[i/beats_per_measure, 0]
                if i%(beats_per_measure) != 0:
                    bassline[0][i] = random.choice(bass_dict[chord_change[i/beats_per_measure, 0]])
            if random.random() < emptiness[1] and i%(beats_per_measure) != 0:
                bassline[0][i] = "."
        bassline = np.asarray(bassline).T

        support = [["."] * beats, ["."] * beats]
        for i in range(0, beats):
            if i%(beats_per_measure/8) == 0:
                chord = [random.choice(arpeggio_dict[chord_change[i/beats_per_measure, 0]]),
                        random.choice(arpeggio_dict[chord_change[i/beats_per_measure, 0]])]
                while chord[1] == chord[0]:
                    print("stuck")
                    chord[1] = random.choice(arpeggio_dict[chord_change[i/beats_per_measure, 0]])
                if bassline[i, 0] == "." and random.random() < emptiness[2] and i%(beats_per_measure/4) == 0:
                    chord = [".", "."]
                support[0][i] = chord[0]
                support[1][i] = chord[1]
        support1 = np.asarray([support[0]]).T
        support2 = np.asarray([support[1]]).T
        print(np.size(support1), np.size(support2), np.size(bassline), np.size(track_0))

        crazybass = [["."] * beats]
        for i in range(0, beats):
            if i%(beats_per_measure/16) == 0:
                crazybass[0][i] = chord_change[i/beats_per_measure, 0]
                if i%(beats_per_measure) != 0:
                    crazybass[0][i] = random.choice(bass_dict[chord_change[i/beats_per_measure, 0]])
            if (random.random() < emptiness[3] and i%(beats_per_measure) != 0) or bassline[i, 0] != ".":
                crazybass[0][i] = "."
        crazybass = np.asarray(crazybass).T

        melody = [["."] * beats]
        for i in range(0, beats):
            if i%(beats_per_measure/4) == 0:
                if random.random() > emptiness[4]:
                    note = random.choice(key_dict[chord_change[i/beats_per_measure, 0]])
                    melody[0][i] = note
        melody = np.asarray(melody).T

        second_melody = [["."] * beats]
        for i in range(0, beats):
            if i%(beats_per_measure/16) == 0:
                if random.random() > (emptiness[5] + 1)/2:
                    note = random.choice(key_dict[chord_change[i/beats_per_measure, 0]])
                    if melody[i, 0] == ".":
                        second_melody[0][i] = note
        second_melody = np.asarray(second_melody).T

        return([track_0, bassline, support1, support2, crazybass, melody, second_melody])"""
