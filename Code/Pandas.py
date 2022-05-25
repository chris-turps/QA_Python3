#pip install pandas
#from typing import Sequence
import pandas as pd

myList = pd.Series([2,4,7]) #creates a zero-labeled list[]
print(f"\nSeries:\n{myList}")

# create some data - a dict...
mydataset = {
  'alphaIndex' : ['a','b','c','d'],
  'cars': ["BMW", "Volvo", "Ford", "Audi"],
  'noInFleet': [3, 7, 2, 9]
}
print(F"Dataset:\n{mydataset}\n")
#make a dataframe:
myFrame = pd.DataFrame(mydataset)
print(f"\nFrame:\n{myFrame}")
# Frames assume we are most interested in columns of data
# Easy access by .name:
print(f"\nOne Col.:\n{myFrame.cars}")
# or by [name] indexing:
print(f"\nOne Col[name]:\n{myFrame['cars']}")
# or by [pos] indexing:
print(f"\nOne Col[pos]:\n{myFrame.iloc[:,1]}")

#.loc[rowLabel]
print(f"\nOne Row[label]:\n{myFrame.loc[1]}")
print(f"\nRow[range]:\n{myFrame.loc[1:3]}")

#.loc[row,col]
print(f"\nOne Col.loc:\n{myFrame.loc[:,'cars']}")
print(f"\nOne Cell:\n{myFrame.loc[1,'cars']}")

#Labeled row-index
myIndex = pd.DataFrame(mydataset, index = ["a","b","c","d"])
print(f"\nIndexedFrame:\n{myIndex}")

# Row by label or position
print(f"\nOne row.loc['b']:\n{myIndex.loc['b']}")
print(f"\nOne row.iloc[1]:\n{myIndex.iloc[1]}")

# Set col as the index
alphaIndexedCopy = myFrame.set_index('alphaIndex')
print(f"\nalphaIndexedCopy:\n{alphaIndexedCopy}")

# Generate new integer index labels
alphaIndexedCopy.reset_index(drop=True,inplace=True)
print(f"\nalphaIndexedCopy:\n{alphaIndexedCopy}")

# Use a new set of labels as row-index
alphaIndexedCopy.insert(0, column='alpha', value=["w","x","y","z"])
print(f"\nmyCol-inserted:\n{alphaIndexedCopy}")
alphaIndexedCopy.set_index('alpha',drop= True, inplace=True)
print(f"\nmyCol-replacing row labels:\n{alphaIndexedCopy}")

#Row filter
print(f"\nrows where noInFleet > 3:\n{alphaIndexedCopy['noInFleet'] > 3}")
print(f"\nmyRow-Filter:\n{alphaIndexedCopy[alphaIndexedCopy['noInFleet'] > 3]}")

#Insert Calculated Columns
alphaIndexedCopy["NewFleet"] = alphaIndexedCopy['noInFleet'] * 2
alphaIndexedCopy["Upgrade"] = alphaIndexedCopy['cars'] + "-turbo"
print(f"\nNewCol:\n{alphaIndexedCopy}")
# Load from various file-types (csv/json etc.)
#.head(n) / .tail(n) # n-lines, default = 5
#.info()
#.dropna() # return copy frame. NA = NotAnything
#.dropna(inplace = True)
#.isna() creates a copy-frame of true/false members
#.fillna(130, inplace = True)

#x = df["Calories"].mean() # calc mean to use as replacement for NA in one col.
#df["Calories"].fillna(x, inplace = True)