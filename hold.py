# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keyboard
import main



alternatel = ['q','3','4','t']
alternater = ['u','9','0','[']

rarel = ['left', 'down', 'plus', '-']
rarer = ['*', 'up arrow', 'i', 'right']

channel1_left = ['space', 's', 'e', 'r']
channel1_right = ['o', 'n', 'i', 't']
channel2_left = ['c', 'l', 'd', 'm']
channel2_right = ['u', 'p', 'g', 'h']
channel3_left = ['b', 'f', 'j', 'w']
channel3_right = ['v', 'k', 'a', 'y']
channel4_left = ['z', 'x', 'backspace', '2']
channel4_right = ['=', ';', 'g', 'enter']

channel5_left = ['', 'k', '9', '=']
channel5_right = ['x', 'r', 'e', 'z']
util_left = ['shift+{', 'shift+}', 'shift+(', 'shift+)']
util_right = ['a', ';', '[', ']']

numl = ['1', '2', '3', '4', '5']
numr = ['6', '7', '8', '9', '0']

keys_left = ['tab', '2', '3', 'r']
keys_right = ['u', '9', '0', '[']

current_mode = ""

def chan1(handler):
    left = channel1_left
    right = channel1_right

    keyboard.remap_key('tab', left[0])

    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])

    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])

def chan2(handler):
    left = channel2_left
    right = channel2_right
    rehook()

    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])


def chan3(handler):
    left = channel3_left
    right = channel3_right
    rehook()
    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])


def chan4(handler):
    left = channel4_left
    right = channel4_right
    rehook()
    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])



def start(name):
    rehook()
    keyboard.wait()


def cHandler(handle):
    left = util_left
    right = util_right
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
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])

def vHandler(handle):
    left = channel2_left
    right = channel2_right
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
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])

def nHandler(handle):
    left = channel4_left
    right = channel4_right
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
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])


def bHandler(handle):
    left = rarel
    right = rarer
    # rehook()
    keyboard.unremap_key('q')
    keyboard.unremap_key('3')
    keyboard.unremap_key('4')
    keyboard.unremap_key('t')

    keyboard.unremap_key('u')
    keyboard.unremap_key('9')
    keyboard.unremap_key('0')
    keyboard.unremap_key('[')

    keyboard.remap_key('q', left[0])
    keyboard.remap_key('3', left[1])
    keyboard.remap_key('4', left[2])
    keyboard.remap_key('t', left[3])

    keyboard.remap_key('u', right[0])
    keyboard.remap_key('9', right[1])
    keyboard.remap_key('0', right[2])
    keyboard.remap_key('[', right[3])

def mHandler(handle):
    left = channel3_left
    right = channel3_right
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
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])


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
    left = channel1_left
    right = channel1_right
    print("hi")
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
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])

def onHandler(handle):
    rehook()

def offHandler(handle):
    keyboard.unhook_all()
    keyboard.on_press_key('delete', onHandler, suppress=True)
    # keyboard.unremap_key('tab')
    # keyboard.unremap_key('2')
    # keyboard.unremap_key('3')
    # keyboard.unremap_key('r')
    # keyboard.unremap_key('u')
    # keyboard.unremap_key('9')
    # keyboard.unremap_key('0')
    # keyboard.unremap_key('[')

def rehook():
    keyboard.unhook_all();
    keyboard.on_press_key('c', cHandler, suppress=True)
    keyboard.on_press_key('v', vHandler, suppress=True)
    keyboard.on_press_key('m', nHandler, suppress=True)
    keyboard.on_press_key(',', mHandler, suppress=True)
    keyboard.on_press_key('b', bHandler, suppress=True)

    keyboard.on_press_key('insert', offHandler, suppress=True)
    keyboard.on_press_key('delete', onHandler, suppress=True)

    left = channel1_left
    right = channel1_right

    # keyboard.remap_key('q', left[0])
    # # keyboard.remap_key('3', left[1])
    # keyboard.remap_key('4', left[2])
    # keyboard.remap_key('t', left[3])
    #
    # keyboard.remap_key('u', right[0])
    # keyboard.remap_key('9', right[1])
    # keyboard.remap_key('0', right[2])
    # keyboard.remap_key('[', right[3])

    keyboard.remap_key('tab', left[0])
    keyboard.remap_key('2', left[1])
    keyboard.remap_key('3', left[2])
    keyboard.remap_key('r', left[3])

    keyboard.remap_key('o', right[0])
    keyboard.remap_key('-', right[1])
    keyboard.remap_key('=', right[2])
    keyboard.remap_key('\\', right[3])

    keyboard.on_release_key('c', releaseHandler, suppress=True)
    keyboard.on_release_key('v', releaseHandler, suppress=True)
    keyboard.on_release_key('m', releaseHandler, suppress=True)
    keyboard.on_release_key(',', releaseHandler, suppress=True)
    keyboard.on_press_key('b', bHandler, suppress=True)

    # keyboard.on_release(releaseHandler, suppress=True)

    # keyboard.on_release(mode, suppress=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm