import keyboard
import csv

words2Fingers = {}
predictor1 = dict()
predictor2 = dict()
lettersBeingCapatalized = []

lastFinisher = " "
previousWord = ""
previousWordCycle = ""

wrote = False
currentFingerPattern = ""
collision_num = 0
lastHash = ""

keysFingerAreOn = ['tab', '2', '3', 'r', 'o', '-', '=', '\\']

mode1 = "aseronit"
mode2 = "cwdmupgh"
mode3 = "bfjwvkqy"
mode4 = "zx"

surroundLeft = ['shift+{', 'shift+}', 'shift+(', 'shift+)']
surroundRight = ['\"', '\'', '[', ']']

arithmeticLeft = ['plus', 'equal', '-', 'underscore']
arithmeticRight = [',', '.', ';', 'shift+;']

numl = ['1', '2', '3', '4', '5']
numr = ['6', '7', '8', '9', '0']


def start(name):
    # Read in the words to fingers file and create map
    wordsMappedToFingersFile = csv.reader(open('hashed_words.csv', 'r'))
    global words2Fingers
    for row in wordsMappedToFingersFile:
        v, k = row
        if k in words2Fingers:
            words2Fingers[k].append(v)
            words2Fingers[k] = sorted(words2Fingers[k])
        else:
            words2Fingers[k] = [v]

    orderedWordsFile = csv.reader(open('predictor-1_word.csv', 'r'))

    # Read in the predictors, which includes a list of words with words that might follow
    global predictor1
    for row in orderedWordsFile:
        k, v = row
        if k in predictor1:
            predictor1[k].append(v)
        else:
            predictor1[k] = [v]

    # This will be the same as above however, the words will be words that came previously
    # reader = csv.reader(open('predictor-2_word.csv', 'r'))
    # global predictor2
    # for row in reader:
    #     v, k = row
    #     if k in predictor2:
    #         predictor2[k].append(v)
    #     else:
    #         predictor2[k] = [v]

    enable()
    keyboard.wait()


def capitalizeHandler(handle):
    keyboard.unhook_key('tab')
    keyboard.unhook_key('2')
    keyboard.unhook_key('3')
    keyboard.unhook_key('r')
    keyboard.unhook_key('o')
    keyboard.unhook_key('-')
    keyboard.unhook_key('=')
    keyboard.unhook_key('\\')

    keyboard.on_press_key('tab', capHandler, suppress=True)
    keyboard.on_press_key('2', capHandler, suppress=True)
    keyboard.on_press_key('3', capHandler, suppress=True)
    keyboard.on_press_key('r', capHandler, suppress=True)
    keyboard.on_press_key('o', capHandler, suppress=True)
    keyboard.on_press_key('-', capHandler, suppress=True)
    keyboard.on_press_key('=', capHandler, suppress=True)
    keyboard.on_press_key('\\', capHandler, suppress=True)


def capHandler(handle):
    finger = str(keysFingerAreOn.index(handle.name) + 1)

    # The current finger pattern
    global currentFingerPattern
    currentFingerPattern = currentFingerPattern + str(finger)

    # Add the letter index for capitalization
    global lettersBeingCapatalized
    lettersBeingCapatalized.append(len(currentFingerPattern) - 1)


def handleSurrounds(handle):
    triggerAlternativeModes('v')


def handleArithmetic(handle):
    triggerAlternativeModes(',')

def periodHandler(handle):
    left = numl
    right = numr
    # rehook()
    keyboard.unremap_key('tab')
    keyboard.unremap_key('2')
    keyboard.unremap_key('3')
    keyboard.unremap_key('r')

    keyboard.unremap_key('o')
    keyboard.unremap_key('-')
    keyboard.unremap_key('=')
    keyboard.unremap_key('\\')

    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('4', left[3])
    keyboard.remap_key('r', left[4])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('0', right[1])
    keyboard.remap_key('-', right[2])
    keyboard.remap_key('=', right[3])
    keyboard.remap_key('\\', right[4])


def releaseHandler(handle):
    enable()


def backspaceHandler(handle):
    global currentFingerPattern
    global previousWord
    global previousWordCycle
    if len(currentFingerPattern) == 0:
        keyboard.press_and_release("backspace")
        previousWordCycle = ""
        previousWord = ""
    else:
        currentFingerPattern = currentFingerPattern[0:len(currentFingerPattern) - 1]


def onHandler(handle):
    enable()


def offHandler(handle):
    keyboard.unhook_all()
    keyboard.on_press_key('delete', turnOn, suppress=True)



def fingerPressed(handle):
    key = str(keysFingerAreOn.index(handle.name) + 1)

    global currentFingerPattern
    global wrote
    global predictor1
    global lettersBeingCapatalized

    if (currentFingerPattern == "" and wrote == True):
        lettersBeingCapatalized = []
        if previousWordCycle != "":
            if previousWordCycle in predictor1:
                predictor1[previousWordCycle].append(previousWord)
            else:
                predictor1[previousWordCycle] = [previousWord]

            # This is writing the new word found
            with open('predictor-1_word.csv', 'w', encoding="UTF-8", newline='') as f:
                writer = csv.writer(f)
                for row in predictor1:
                    v = predictor1[row]
                    for value in set(v):
                        writer.writerow([row, value])

    wrote = False
    currentFingerPattern = currentFingerPattern + str(key)
    print("my current string is " + currentFingerPattern)

def capitalize_n(text, pos):
    before_nth = text[:pos]
    n = text[pos].upper()
    new_pos = pos + 1
    after_nth = text[new_pos:]
    return before_nth + n + after_nth


def cycleStrings(handle):
    global currentFingerPattern
    global lastString
    global lettersBeingCapatalized
    global collision_num
    global lastFinisher
    global lastHash
    global previousWord

    try:
        print(lastString)
        collision_num += 1
        if lastString != "" and collision_num < len(words2Fingers[lastString]):
            keyboard.press_and_release("backspace")
            for c in lastHash:
                keyboard.press_and_release("backspace")
            string_of_hash = words2Fingers[lastString][collision_num]
            for c in lettersBeingCapatalized:
                string_of_hash = capitalize_n(string_of_hash, c)
            lastHash = string_of_hash
            previousWord = string_of_hash
            keyboard.write(string_of_hash)
            keyboard.write(lastFinisher)
            print(words2Fingers[lastString])
        if collision_num == len(words2Fingers[lastString]) - 1:
            collision_num = -1

    except KeyError:
        currentFingerPattern = ""


def finishHandler(handle):
    global currentFingerPattern
    global lastString
    global lastFinisher
    global lettersBeingCapatalized
    global collision_num
    global previousWord
    global previousWordCycle
    global wrote
    global lastHash
    global predictor1

    string_of_hash = ""
    try:
        if currentFingerPattern != "":
            string_of_hash = words2Fingers[currentFingerPattern][0]
            lastString = currentFingerPattern
            lastHash = string_of_hash

            previousWordCycle = previousWord
            if previousWordCycle in predictor1:
                predictions = predictor1[previousWordCycle]
                for value in words2Fingers[currentFingerPattern]:
                    if value in predictions:
                        string_of_hash = value

            for c in lettersBeingCapatalized:
                string_of_hash = capitalize_n(string_of_hash, c)

            previousWord = string_of_hash

            keyboard.write(string_of_hash)
            wrote = True
            if handle.name == "space":
                keyboard.write(" ")
                lastFinisher = " "
            else:
                keyboard.write(handle.name)
                lastFinisher = handle.name
            print(words2Fingers[currentFingerPattern])

    except KeyError:
        currentFingerPattern = ""

    collision_num = 0
    currentFingerPattern = ""

def turnOn(handle):
    enable()


def turnOff(handle):
    keyboard.unhook_all()
    keyboard.on_press_key('delete', turnOn, suppress=True)


def presser(handle):
    keyboard.press("shift+[")


def triggerAlternativeModes(mode):
    keyboard.unhook_all()

    # Turn on modes
    keyboard.on_press_key('c', capitalizeHandler, suppress=True)
    keyboard.on_press_key('v', handleSurrounds, suppress=True)
    keyboard.on_press_key(',', handleArithmetic, suppress=True)

    # On release, should return to standard mode
    keyboard.on_release_key('c', releaseHandler, suppress=True)
    keyboard.on_release_key('v', releaseHandler, suppress=True)
    keyboard.on_release_key(',', releaseHandler, suppress=True)

    # Turn on off still should work
    keyboard.on_press_key('insert', turnOff, suppress=True)
    keyboard.on_press_key('delete', turnOn, suppress=True)

    # v mode handler
    if mode == 'v':
        left = surroundLeft
        right = surroundRight
        keyboard.remap_key('tab', left[0])
        keyboard.remap_key('2', left[1])
        keyboard.remap_key('3', left[2])
        keyboard.remap_key('r', left[3])

        keyboard.remap_key('o', right[0])
        keyboard.remap_key('-', right[1])
        keyboard.remap_key('=', right[2])
        keyboard.remap_key('\\', right[3])

    # comma handler
    if mode == ',':
        left = arithmeticLeft
        right = arithmeticRight
        keyboard.remap_key_no_suppress('tab', left[0])
        keyboard.remap_key_no_suppress('2', left[1])
        keyboard.remap_key_no_suppress('3', left[2])
        keyboard.remap_key_no_suppress('r', left[3])

        keyboard.remap_key_no_suppress('o', right[0])
        keyboard.remap_key_no_suppress('-', right[1])
        keyboard.remap_key_no_suppress('=', right[2])
        keyboard.remap_key_no_suppress('\\', right[3])

    keyboard.on_press_key('space', finishHandler, suppress=True)
    keyboard.on_press_key('backspace', backspaceHandler, suppress=True)

def enable():
    # Setup manual modes
    keyboard.unhook_all();
    keyboard.on_press_key('c', capitalizeHandler, suppress=True)
    keyboard.on_press_key('v', handleSurrounds, suppress=True)
    keyboard.on_press_key('.', cycleStrings, suppress=True)
    keyboard.on_press_key(',', handleArithmetic, suppress=True)

    # When these keys are release, we should return to the
    # standard mode.
    keyboard.on_release_key('c', releaseHandler, suppress=True)
    keyboard.on_release_key('v', releaseHandler, suppress=True)
    keyboard.on_release_key('b', releaseHandler, suppress=True)
    keyboard.on_press_key(',', releaseHandler, suppress=True)

    # Modes for on/off
    keyboard.on_press_key('insert', turnOff, suppress=True)
    keyboard.on_press_key('delete', turnOn, suppress=True)

    # Enable on key press for all your fingers
    # If you want to change fingers, change above
    keyboard.on_press_key(keysFingerAreOn[0], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[1], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[2], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[3], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[4], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[5], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[6], fingerPressed, suppress=True)
    keyboard.on_press_key(keysFingerAreOn[7], fingerPressed, suppress=True)

    #lmany
    # Many of these should be removed except the space
    # When the space is pressed, the finish handler is called
    keyboard.on_press_key('space', finishHandler, suppress=True)
    # keyboard.on_press_key('[', finishHandler, suppress=True)
    # keyboard.on_press_key(']', finishHandler, suppress=True)
    # keyboard.on_press_key('(', finishHandler, suppress=True)
    # keyboard.on_press_key(')', finishHandler, suppress=True)
    # keyboard.on_press_key('.', finishHandler, suppress=True)
    # keyboard.on_press_key('\"', finishHandler, suppress=True)
    # keyboard.on_press_key('+', finishHandler, suppress=True)
    # keyboard.on_press_key('-', finishHandler, suppress=True)
    # keyboard.on_press_key('backspace', backspaceHandler, suppress=True)

if __name__ == '__main__':
    start('PyCharm')
