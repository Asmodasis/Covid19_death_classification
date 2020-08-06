from numpy.random import choice

datasetFile = 'daily.csv'

trainFile   = './dataset/covid-train-data.csv'                                                         # files for the data sets
testFile    = './dataset/covid-test-data.csv'
valFile     = './dataset/covid-val-data.csv'
trainWeight = 0.60
testWeight  = 0.20
valWeight   = 0.20

with open(datasetFile) as covidFile:                                                                    # open the csv file
    next(covidFile)
#covidFile = open(datasetFile)   
#next(covidFile)                                                                                         # skip the header

    with open(trainFile, "w") as train, open(testFile, "w") as test, open(valFile, "w") as val:         # create new files for the train/test/val sets
        for line in covidFile:                                                                          # read the lines in the file
            f = choice([train,test,val],1, p=[trainWeight,testWeight,valWeight])             # split the data sets, favour training set.
            #for i in range(2):
                                                            
                #print(f)
            f.write(line)                                                                               # write to the new location
#covidFile.close()