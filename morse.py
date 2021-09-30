import math
import wave
import struct
import sys
import getopt
import re
import subprocess, os, platform

samplerate = 44100.0  # Hertz	

class Audio:
	def __init__(self):
		self.audio = []
		return

	def appendSilence(self, duration):
    		numSamples = duration * (samplerate / 1000.0)
    		for x in range(int(numSamples)): 
        		self.audio.append(0.0)
    		return

	def appendSinewave(self, duration):
    		numSamples = duration * (samplerate / 1000.0)
    		for x in range(int(numSamples)):
        		self.audio.append(1.0 * math.sin(2 * math.pi * 440.0 * ( x / samplerate )))
    		return

	def saveWav(self, filename):
		wavFile=wave.open(filename,"w")
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

def generateAudio(inputText, filename, play):
	outputFile = Audio()
	if Audio is not None:
		for c in inputText:
			print ("Generating audio...")
			print (c)
			if (c == ' '):
                        	outputFile.appendSilence(100*3)
                        	print ("appending 3 silences...")
			else:
				for b in (morse[c]):
					if b == ".":
						outputFile.appendSinewave(100)
						print ("appending short sinewave...")	
						outputFile.appendSilence(100)
						print ("appending silence...")
					elif b == "-":
						outputFile.appendSinewave(500)
						print ("appending long sinewave...")
						outputFile.appendSilence(300)
						print ("appending silence...")
		print("success!")
		outputFile.saveWav(filename)
		if (play):
			if platform.system() == 'Darwin':       # macOS
    				subprocess.call(('open', filename))
			elif platform.system() == 'Windows':    # Windows
    				os.startfile(filename)
			else:                                   # linux variants
    				subprocess.call(('xdg-open', filename))	

#- = Long, . = Short

morse = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	"10": "..-."
	}

def readMessage(argv):
	text = False
	audio = False
	inputFile = ''
	inputText = ''
	outputFile = 'output.wav'
	play = False
	try:
		opts, args = getopt.getopt(argv, "htapi:o:" ,["inputText=","outputFile=","inputFile=","play", "audio", "text"])
	except getopt.GetoptError:
		print("usage: morse.py \n -i or --inputText <'inputText'> \n -t or --text to output text \n -a or --audio to output audio \n -o or --outputFile <outputFile> to specify filename for audio (default is output.wav)")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("usage: morse.py \n -i or --inputText <'inputText'> \n -t or --text to output text \n -a or --audio to output audio \n -o or --outputFile <outputFile> to specify filename for audio (default is output.wav)")
			sys.exit()
		elif opt in ("-i", "--inputText"):
			inputText = arg
		elif opt in ("-o", "--outputFile"):
			outputFile = arg
		elif opt in ("-a", "--audio"):
			audio = True
		elif opt in ("-t", "--text"):
			text = True
		elif opt in ("-p", "--play"):
			play = True
	if (inputText == ''):
		print("You need to provide input text using the -i parameter")
	if (text):
		generateText(inputText.upper())
	if (audio): 
		generateAudio(inputText.upper(), outputFile, play)


	

def generateText(inputText):
	outputText = ''
	for c in inputText:
		if c == ' ':
			outputText += " "
		else:	
			outputText += morse[c]
			outputText += " "
	print(outputText)

if __name__ == "__main__":
	readMessage(sys.argv[1:])





















