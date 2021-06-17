def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("TANUJ MANRAL\n")
                myfile.write("NIDHI MANRAL\n")
                myfile.write("RAHUL MANRAL\n")
                myfile.write("KAVYA MANRAL")
        txt = open(fname)
        print(txt.read())
file_read('abcdef.txt')