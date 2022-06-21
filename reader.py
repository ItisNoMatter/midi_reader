import music21 as m21
mf = m21.midi.MidiFile()
mf.open('midifiles/bach_846.mid')
mf.read()
for event in mf.tracks[3].events:
    if type(event) == m21.midi.MidiEvent:
        print("pitch:"+str(event.pitch)+"   time:"+str(event.time))
