import copy

f = open("../data/data.txt", "r")
data = f.read()

# compute character frequency
tempFreq = {}
for letter in data:
    if letter in tempFreq:
        tempFreq[letter] += 1
    else:
        tempFreq[letter] = 1
freq = sorted(tempFreq.items(), key=lambda x: x[1], reverse=True)
freqVal = list(map(lambda x: {"val": x[0], "freq": x[1]}, freq))


# create a binary tree
i = 2
while i > 1:
    # sort based on character frequency
    freqVal = sorted(freqVal, key=lambda x: x["freq"], reverse=True)
    i = len(freqVal) - 2

    # replace i'th node
    freqVal[i] = {
        "val": [freqVal[i]["val"], freqVal[i + 1]["val"]],
        "freq": freqVal[i]["freq"] + freqVal[i + 1]["freq"],
    }

    # delete i-1 node as it is already copied in node created above
    del freqVal[len(freqVal) - 1]

# select left and right values
tree = [freqVal[0]["val"], freqVal[1]["val"]]


# encode
encodedChars = {}


def recursiveEncode(values, id):
    if len(values) == 1:
        encodedChars[values[0]] = list(id)
    else:
        idLeft = list(id)
        idRight = list(id)

        idLeft.append(0)
        idRight.append(1)

        recursiveEncode(values[0], idLeft)
        recursiveEncode(values[1], idRight)


# decode
text = []
idx = 0


def recursiveDecode(values, id):
    global idx, tree, encodedText

    side = id[0]
    idx += 1

    if len(values[side]) == 1:
        text.append(values[side])
        return True
    elif recursiveDecode(values[side], id[1 : len(id)]) and (
        idx < len(encodedText) - 1
    ):
        recursiveDecode(tree, encodedText[idx:])


recursiveEncode(tree, [])

encodedText = []
for letter in data:
    encodedText.extend(encodedChars[letter])

recursiveDecode(tree, encodedText)

print("Encoded - \n" + "".join(str(s) for s in encodedText))
print("\nDecoded - \n"+"".join(text))
print("\nOriginal string size - " + str(len(text) * 8)+"Bytes")
print("Compressed string size - " + str(len(encodedText))+"Bytes")
