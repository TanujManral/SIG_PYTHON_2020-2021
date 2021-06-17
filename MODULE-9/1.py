
def LastNlines(fname, N):
	with open(fname) as file:
		
		for line in (file.readlines() [-N:]):
			print(line, end ='')
if __name__ == '__main__':
	fname = 'abcdef.txt'
	N = 4
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
