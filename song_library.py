import numpy as np
import random

def song_sample_1():
    """Short song sample. Recommended tempo: 240 bpm."""

    track_0 = silence(8)
    track_1 = np.asarray(["C3 . . . G3 . . .".split()]).T
    track_2 = np.asarray(["Eb4 . F4 Eb4 D4 . F4 Eb4".split()]).T
    track_3 = np.asarray(["C5 G5 C6 G5 D5 G5 D6 ".split()]).T
    return [track_0, track_1, track_2, track_3]

def mario():
    track_0 = silence(16)
    track_1 = np.asarray(["A4 A4 . A4 . F4 A4 . C5 . . . C4 . . .".split()]).T
    return [track_0, track_1]

def final_countdown():
    """ Sample from 'The Final Countdown.' Recommended tempo: 480 bpm."""

    measures = 12
    track_0 = silence(16 * measures)

    track_1 = np.asarray([(" A2 .  .  .  .  .  .  .  .  .  .  .  G2 .  .  . " +
                        "    F2 .  .  .  .  .  .  .  .  .  .  .  E2 .  .  . " +
                        "    D2 .  .  .  .  .  .  .  .  .  .  .  D2 .  .  . " +
                        "    G2 .  .  .  .  .  .  .  G#2 . .  .  .  .  .  . " +

                        "    A2 .  .  .  .  .  .  .  .  .  .  .  G2 .  .  . " +
                        "    F2 .  .  .  .  .  .  .  .  .  .  .  E2 .  .  . " +
                        "    D2 .  .  .  .  .  .  .  .  .  .  .  D2 .  .  . " +
                        "    G2 .  .  .  .  .  .  .  G#2 . .  .  .  .  .  . " +

                        "    A2 .  .  .  .  .  .  .  B2 .  .  .  .  .  .  . " +
                        "    C3 .  B2 .  A2 .  G2 .  F2 .  .  .  F2 .  .  . " +
                        "    E2 .  .  .  B2 .  .  .  B2 .  .  .  B2 .  .  . " +
                        "    E2 .  .  . G#2 .  .  . G#2 .  .  . G#2 .  .  .").split()]).T


    track_2 = np.asarray([(" A3 . " * 8                                        +
                        "    F3 . " * 8                                        +
                        "    D3 . " * 8                                        +
                        "    B3 . " * 8                                        +

                        "    A3 . " * 8                                        +
                        "    F3 . " * 8                                        +
                        "    D3 . " * 8                                        +
                        "    B2 . " * 8                                        +

                        "    C3 .  .  .  .  .  .  .  B2 .  .  .  .  .  .  . " +
                        "    G3 .  .  .  G3 .  .  .  F3 .  .  .  A3 .  .  . " +
                        "    A3 .  E4 .  E4 .  E4 .  E4 .  E4 .  E4 .  E4 . " +
                        "    G#3 . E4 .  E4 .  E4 .  E4 .  E4 .  E4 .  E4 . ").split()]).T

    track_3 = np.asarray([(" C5 .  .  .  C4  .  E5 D5 E5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  F5 E5 F5 .  E5 .  D5 .  .  . " +
                        "    .  .  .  .  .  .  F5 E5 F5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  D5 C5 D5 .  C5 .  B4 .  D5 . " +

                        "    C5 .  .  .  .  .  E5 D5 E5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  F5 E5 F5 .  E5 .  D5 .  .  . " +
                        "    .  .  .  .  .  .  F5 E5 F5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  D5 C5 D5 .  C5 .  B4 .  D5 . " +

                        "    C5 .  .  .  .  .  B4 C5 D5 .  .  .  .  .  C5 D5" +
                        "    E5 .  D5 .  C5 .  B4 .  A4 .  .  .  F5 .  .  . " +
                        "    E5 .  .  .  .  .  .  .  .  .  .  .  E5 F5 E5 D5" +
                        "    E5 .  .  .  A3 .  A3 .  C4 .  .  .  B3 .  .  . ").split()]).T

    track_4 = np.asarray([(" B4 .  .  .  A4 .  A4 .  C5 .  .  .  E4 .  .  . " +
                        "    .  .  .  .  .  .  C5 .  C5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  D5 .  D5 .  .  .  F4 .  .  . " +
                        "    .  .  .  .  .  .  B4 .  B4 .  .  .  G4 .  .  . " +

                        "    C4 .  .  .  .  .  A4 .  C5 .  .  .  E4 .  .  . " +
                        "    .  .  .  .  .  .  C5 .  C5 .  .  .  A4 .  .  . " +
                        "    .  .  .  .  .  .  D5 .  D5 .  .  .  F4 .  .  . " +
                        "    .  .  .  .  .  .  B4 .  B4 .  .  .  G4 .  .  . " +

                        "    A4 .  .  .  .  .  G4 .  .  .  .  .  .  .  .  . " +
                        "    C5 .  D5 .  C5 .  B4 .  F4 .  .  .  C5 .  .  . " +
                        "    B4 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . " +
                        "    B4 .  .  .  A4 .  A4 .  C5 .  .  .  B4 .  .  . ").split()]).T

    track_5 = np.asarray([(" E6 C6 A5 C6 E6 C6 A5 C6 E6 C6 A5 C6 E6 C6 A5 C6" +
                        "    F6 C6 A5 C6 F6 C6 A5 C6 F6 C6 A5 C6 F6 C6 A5 C6" +
                        "    F6 D6 A5 D6 F6 D6 A5 D6 F6 D6 A5 D6 F6 D6 A5 D6" +
                        "    G6 D6 B5 D6 G6 D6 B5 D6 G6 D6 B5 D6 G6 D6 B5 D6" +

                        "    E6 C6 A5 C6 E6 C6 A5 C6 E6 C6 A5 C6 E6 C6 A5 C6" +
                        "    F6 C6 A5 C6 F6 C6 A5 C6 F6 C6 A5 C6 F6 C6 A5 C6" +
                        "    F6 D6 A5 D6 F6 D6 A5 D6 F6 D6 A5 D6 F6 D6 A5 D6" +
                        "    G6 D6 B5 D6 G6 D6 B5 D6 G6 D6 B5 D6 G6 D6 B5 D6" +

                        "    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . " +
                        "    E6 .  D6 .  C6 .  B5 .  A5 .  .  .  F6 .  .  . " +
                        "    E6 B5 A5 B5 E6 B5 A5 B5 E6 B5 A5 B5 E6 B5 A5 B5" +
                        "    E6 B5 Ab5 B5 E6 B5 Ab5 B5 E6 B5 Ab5 B5 E6 B5 Ab5 B5").split()]).T

    print(len(track_0), len(track_1), len(track_2), len(track_3), len(track_4), len(track_5))
    return [track_0, track_1, track_2, track_3, track_4, track_5]

def silence(num_beats):
    rests = ". " * num_beats
    return np.asarray([rests.split()]).T

def random_song():
    measures = 4
    beats_per_measure = 16
    beats = beats_per_measure * measures
    normalization_factor = 0.5
    bass_emptiness = random.random() * (1-normalization_factor) + 0.5 * normalization_factor
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

    return([track_0, bassline, support1, support2, crazybass, melody, second_melody])
