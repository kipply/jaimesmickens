import os

f = open("training_data.txt", "w")

for subdir, dirs, files in os.walk('data'):
    for file in files:
    	r = open('data/' + file, "r").read()
    	f.write(r.replace("\n\n", "\n"))
