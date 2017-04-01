import os

filenames = os.listdir('./')
for i in range(len(filenames)):
	name = filenames[i]
	if name[len(name)-1] is 'c':
		name_for = name[0:len(name)-2]
		print name_for
		new_name = name_for + 'cpp'
		print new_name
		os.rename(name, new_name)
