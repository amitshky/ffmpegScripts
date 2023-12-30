import os
from pathlib import Path

def main():
	pathList = list(Path('.').glob('./*.mov'))
	outDir = './out/'
	if not os.path.exists(outDir):
		os.makedirs(outDir)
		
		for path in pathList:
			pathStr = str(path)
			filename = os.path.basename(pathStr)
			
			command = f'ffmpeg -i "{pathStr}" "out/{filename}'
			print(command)
			#os.system(command)
			
	else:
		print('"out" directory already exists. Rename the output directory or move the contents of the existing "out" directory.')



if __name__ == '__main__':
	main()
