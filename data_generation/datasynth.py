
from synthesizer import Writer, Synthesizer, Waveform
from random import randrange

#setup audio classes
writer = Writer()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

#sample parameters
NUM_SAMPLES = 2000
LOW_HZ = 20
HIGH_HZ = 20000


for s in range(NUM_SAMPLES):
	note = randrange(20,20000)
	wave = synthesizer.generate_constant_wave(note, 3.0)
	writer.write_wave("./samples/" + str(note) + "Hz.mp3", wave)
	print(s)