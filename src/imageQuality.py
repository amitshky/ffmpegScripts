import os
import argparse
from pathlib import Path


def main():
	parser = argparse.ArgumentParser(description='Compress images (JPEG) in a directory and its sub-directory if the image filesize is greater than value provided in the command line argument (default is 700KB).')
	parser.add_argument('-q', '--quality',  type=int, default=2,   metavar='', help='Quality value for compression; normal range for JPEG is 2-31; higher value means lower quality')
	parser.add_argument('-f', '--filesize', type=int, default=700, metavar='', help='Images higher than this value will be compressed; provide size in KB')
	args = parser.parse_args()

	# without conversion to list, the loop iterates over "out" directory and 
	# processes the images that have already been processed,
	# creating a new "out" directory inside the existing "out" directory
	pathlist = list(Path('.').glob('**/*.jpg'))

	outDir = './out/'
	if not os.path.exists(outDir):
		os.makedirs(outDir)

		for path in pathlist:
			pathStr = str(path)                        # returns "folderName\filename.extension"
			filename = os.path.basename(pathStr)       # returns "filename.extension"
			foldername = pathStr.replace(filename, '') # returns "folderName\"

			if os.path.getsize(pathStr) > (args.filesize * 1024):
				# create directory in the 'out' directory according to input directory structure
				outDir = './out/' + foldername
				if not os.path.exists(outDir):
					os.makedirs(outDir)
				
				# ffmpeg command
				command = f'ffmpeg -i "{pathStr}" -q:v {args.quality} "out\{pathStr}"'
				print(command)     # print the command
				os.system(command) # execute command in the terminal
	else:
		print('"out" directory already exists. Rename the output directory or delete the existing "out" directory.')


if __name__ == '__main__':
	main()