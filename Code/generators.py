import glob
import os

pattern = r"C:\Users\Stephen\Documents\,AStephen_Other\QA\QAPYTH3 Python 3\*"

for fname in filter(os.path.isdir, glob.iglob(pattern)):
#for fname in glob.iglob(pattern):
    print( '\n', fname)

dirs = list(filter(os.path.isdir, glob.iglob(pattern)))
print('\n',dirs)

sizes = [os.path.getsize(fname) for fname in glob.iglob(pattern)]

print('\n',sizes)

names = {fname:len(fname) for fname in glob.iglob(pattern) if fname.endswith('2.5') }

print('\n',names)

mytuple = tuple([os.path.getsize(fname) for fname in glob.iglob(pattern)])
print('\n',mytuple)

for result in [os.path.getsize(fname) for fname in glob.iglob(pattern)]:
    print('\n',result)

def get_dir(pattern):
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            yield os.path.basename(file)
        else:
            continue

def get_dir_compr(pattern):
    return (os.path.basename(fname) for fname in glob.iglob(pattern) if os.path.isdir(fname))

for folder in get_dir(pattern):
    print("lazy: ", folder)

for folder in get_dir_compr(pattern):
    print("lazy comprehension: ", folder)

result_list = list(get_dir_compr(pattern))
print("\nresult_list: ", result_list)

myDirPatternGen = get_dir_compr(pattern)
print("\nResult is:",myDirPatternGen)

newVal = next(myDirPatternGen)
print("\nresult 1: ", newVal)
newVal = next(myDirPatternGen)
print("\nresult 2: ", newVal) 
newVal = next(myDirPatternGen)
print("\nresult 3: ", newVal)
newVal = next(myDirPatternGen)
print("\nresult 4: ", newVal) 