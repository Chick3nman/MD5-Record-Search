
__authors__ = ['Chick3nputer', 'Supersam654']

from itertools import islice, product
import string
import hashlib
import multiprocessing
from multiprocessing import Process
from random import shuffle
from sys import argv

chars = "0123456789abcdef"

def generate_strings(size):
    alphabet = list(chars * size)
    while True:
        shuffle(alphabet)
        for i in range(0, len(alphabet), size):
            yield ''.join(alphabet[i: i + size])

def tsum(hexhash):
    return sum(int(hexhash[i: i + 2], 16) for i in range(0, len(hexhash), 2))

def edit_distance(h1, h2):
    xor = int(h1, 16) ^ int(h2, 16)
    return bin(xor)[2:].count('1')

def work():
    # Start both not at 0 and 128 to avoid a lot of startup noise.
    max_ones = 109
    min_ones = 19
    rand_length = 32
    i = 0
    for combo in generate_strings(rand_length):
        i += 1
        if i % 100000000 == 0:
            print "Processed %d hashes." % i
        clear = combo
        hashhex = hashlib.md5(clear).hexdigest()

        ones_count = bin(int(hashhex, 16))[2:].count('1')
        if ones_count > max_ones:
            plain = hashhex + ':' + clear
            max_ones = ones_count
            print "New BITMAX Hash Found %s = %s" % (plain, max_ones)
        elif ones_count < min_ones:
            plain = hashhex + ':' + clear
            min_ones = ones_count
            print "New BITMIN Hash Found %s = %s" % (plain, min_ones)

        if hashhex.startswith('ffffffffffffff'):
            print "New MAX Hash Found %s:%s" % (hashhex, clear)
        elif hashhex.startswith('00000000000000'):
            print "New MIN Hash Found %s:%s" % (hashhex, clear)

        tsumhex = tsum(hashhex)
        if tsumhex < 190:
            print "New TMIN Hash Found %s:%s" % (hashhex, clear)
        elif tsumhex > 3909:
            print "New TMAX Hash Found %s:%s" % (hashhex, clear)

        base_distance = edit_distance(hashhex, '0123456789abcdeffedcba9876543210')
        if base_distance < 20:
            print "New BASE Hash Found %s:%s" % (hashhex, clear)
            
        fp_distance = edit_distance(clear, hashhex)
        if fp_distance < 26:
            print "New FP Hash Found %s:%s" % (hashhex, clear)

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    for i in range(0, count):
        p = Process(target=work)
        p.start()
        print "Starting worker %s" % (i+1)
