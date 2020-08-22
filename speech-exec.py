import math
import wave
import struct

samplerate = 44100.0  # Hertz	

class Audio:
	def __init__(self):
		self.audio = []
		return

	def appendSilence(self):
    		numSamples = 500 * (samplerate / 1000.0)
    		for x in range(int(numSamples)): 
        		self.audio.append(0.0)
    		return

	def appendSinewave(self, duration):
    		numSamples = duration * (samplerate / 1000.0)
    		for x in range(int(numSamples)):
        		self.audio.append(1.0 * math.sin(2 * math.pi * 440.0 * ( x / samplerate )))
    		return

	def saveWav(self):
		wavFile=wave.open("debug.wav","w")
		wavFile.setparams((
			1, #nchannels
			2, #sampwidth
			samplerate,
			len(self.audio), #nframes
			"NONE",#comptype
			"not compressed")) #compname
		for sample in self.audio:
			wavFile.writeframes(struct.pack('h', int( sample * 32767.0 )))
		wavFile.close()
		return

test = Audio()
if Audio is not None:
	print ("Success!")
print ("Generating audio...")
test.appendSinewave(500)
print ("appending sinewave...")
test.appendSilence()
print ("appending silence...")
test.appendSinewave(300);
print ("appending sinewave...")
test.saveWav()

#L = Long, S = Short
streetno = {}
streetno["A"] = "LS"
streetno["B"] = "LSSS"
streetno["C"] = "LSLS"
streetno["D"] = "LSS" 
