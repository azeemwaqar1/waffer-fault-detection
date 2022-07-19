from os import listdir
i=0
for f in listdir("Training_Batch_Files"):
    i = i+1
print(i)
i = 0
for f in listdir("Good_Raw_Files"):
    i = i + 1
print(i)
i = 0
for f in listdir("Bad_Raw_Files"):
    i = i + 1
print(i)
