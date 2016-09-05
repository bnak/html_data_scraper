from sys import argv
import re
import random
#script, filename = argv


def read_file(my_file):

    f = open(my_file)
    filetext = f.read()
    #filetext = re.sub('[,)(_]', "", filetext)

    f.close()

    return filetext


