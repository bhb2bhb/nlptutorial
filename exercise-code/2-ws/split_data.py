'''
This file split the file: data/rmrb-199812.tok into
two separate files named:
- rmrb-train.tok
- rmrb-test.tok
'''
filePath = "../../data/rmrb-199812.tok"
trainPath = "../../data/rmrb-train.tok"
testPath = "../../data/rmrb-test.tok"

f_origin = open(filePath, "r")
lines = f_origin.readlines() # list

# shuffle lines randomly
import random
random.shuffle(lines)

# get the first 1000 lines as test
# and the rest as train
test = lines[:1000]
train = lines[1000:]

# save test with '|||' to separate test sentence
# and golden answer
f_test = open(testPath, "w")
for sentence in test:
	testSent = "".join(sentence.split())
	goldSent = sentence
	line = testSent + " ||| " + goldSent
	f_test.write(line)

f_train = open(trainPath, "w")
for sentence in train:
	f_train.write(sentence)