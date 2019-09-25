import os
import subprocess

class ConverterScript:
	"""Converts MP4s to MP3s"""

	def __init__(self):
		self.curdur = os.getcwd()
		self.inputDirectory = self.curdur + '/inputs'
		self.fileList = os.listdir(self.inputDirectory)
		self.ffmpegDir = self.curdur + "/FFMPEG/ffmpeg/bin/ffmpeg"
		self.totalNumberOfFiles = len(self.fileList)

	# returns current working directory
	def getCurdur(self):
		return self.curdur

	# returns the directory where mp4 inputs are located
	def getInputDirectory(self):
		return self.inputDirectory

	# returns directory where ffmpeg program is located
	def getFfmpegDir(self):
		return self.ffmpegDir

	# prints completion
	def printPercentComplete(self, i):
		percentComplete = (i / float(self.totalNumberOfFiles)) * 100
		print (".\n" * 5) + "%.2f percent complete" % percentComplete

	# converts files
	def convert(self):
		counter = 1

		for file in self.fileList:
			if ".mp4 in file":
				newFileName = file[:-4] + ".mp3"
				subprocess.call([self.ffmpegDir, "-i", ("" + self.getCurdur() + "/inputs/" + file), newFileName])
				self.printPercentComplete(counter)
				counter += 1

