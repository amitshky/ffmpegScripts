import os
import argparse
from pathlib import Path


def main():
	parser = argparse.ArgumentParser(description='Change/Add album art in audio files in a directory and its sub-directory.')
	parser.add_argument('-c',  '--cover',       type=str, default='Cover.jpg',  metavar='', help='Album art cover pic')
	parser.add_argument('-e',  '--extension',   type=str, default='flac',  metavar='', help='Audio file extension')
	args = parser.parse_args()

	pathList = list(Path('.').glob(f'**/*.flac'))

	outDir = './out/'
	if not os.path.exists(outDir):
		os.makedirs(outDir)

		for path in pathList:
			pathStr = str(path)
			filename = os.path.basename(pathStr)
			foldername = pathStr.replace(filename, '')

			outDir = './out/' + foldername
			if not os.path.exists(outDir):
				os.makedirs(outDir)
			
			command = f'ffmpeg -i "{pathStr}" -i Cover.jpg -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "out/{pathStr}"'
			print(command)
			os.system(command)
	else:
		print('"out" directory already exists. Rename the output directory or move the contents of the existing "out" directory.')


if __name__ == '__main__':
	main()