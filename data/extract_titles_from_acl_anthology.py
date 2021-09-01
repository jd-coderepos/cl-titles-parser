import sys

def read_file(input_file, out_filename):	

	output_file = open(out_filename, 'w', encoding='utf-8')
	
	with open(input_file, 'r', encoding='utf-8') as f:
		while(True):
			line = f.readline().rstrip("\n")
			if line:
				if ' title =' in line:
					title = line.split("=")[1].lstrip(" \"").rstrip("\",")
					title = title.replace('{', '').replace('}', '')
					
					if '' == title:
						continue					
					
					output_file.write(title+'\n')
			else:
				break
			
def main(argv):
	#the argument should be a file with a list of titles
	
	if not len(argv) == 2:
		print('Usage: python parse_titles.py <anthology.bib> <output-filename>')
	else:
		read_file(argv[0], argv[1])

		
if __name__ == "__main__":
    main(sys.argv[1:])