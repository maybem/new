

import fnmatch
import os

def findFilesMatching(dir,matchingPattern):
	oldNames = []
	for root, dirnames, filenames in os.walk(dir):
		for filename in fnmatch.filter(filenames, matchingPattern):
			oldNames.append(os.path.join(root, filename))
	return oldNames

dir = 'D:/foto/test/'
matchingPattern = '_rank'
replaceTo='_rate'

# oldNames = 
oldNames = findFilesMatching(dir,'*'+matchingPattern+'*')
print (oldNames)
for oldName in oldNames:
	print(oldName)
	newName=oldName.replace(matchingPattern,replaceTo)
	print(newName)
	os.rename(oldName,newName)


# dir= 'C:/Users'
# for f in glob.glob('*_rank.jpg'):
	
	# new_filename= f.replace('*_rank','*_rate')
	# os.rename(f,new_filename)