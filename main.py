import subprocess
import os

def main():
	curdur = os.getcwd()
	inputDirectory = curdur + '/inputs'
	fileList = os.listdir(inputDirectory)
	ffmpegDir = curdur + "/FFMPEG/ffmpeg/bin/ffmpeg"
	
	print ffmpegDir
	
	counter = 1
	totalNumberOfFiles = len(fileList)
	
	for file in fileList:
		if ".mp4" in file and not os.path.isfile(file[:-4] + "MP3.mp3"):
			percentComplete = (counter / float(totalNumberOfFiles)) * 100
			newFileName = file[:-4] + "MP3.mp3"
			subprocess.call([ffmpegDir, "-i", ("/Users/connorreitz/Documents/Programming/convertMP4toMP3/inputs/1.1_Growth_Adaptations.mp4"), newFileName])
			print (".\n" * 5) + "%.2f percent complete" % percentComplete + (".\n" * 5)
		
		counter += 1		
		
main()