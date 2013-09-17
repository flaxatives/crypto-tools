Crypto Tools
============

Overview
--------
This is mainly a bunch of programs and scripts in Python
that I've developed to supplement my learning in Cryptography 1
at Virginia Tech. Many scripts can be used on the command line
and as a module. There's some good stuff in here that can actually
be useful outside of class, like the letter frequency count.

Contents
--------

+   hw1/ - mostly unintelligible blabber about some substitution
ciphers. The scripts in this directory don't really do anything but
do frequency counts
+   hw2/ - directory containing probably the most useful modules:
letter frequency count and alpha-index conversion. also includes an
example for Vigenere cipher analysis (problem1.py).
+   hw2/frequency.py - a useful module that counts alphanumeric characters.
Can be used from the command line like so:

        $ ./frequency.py this is a string
        Total alpha chars: 13
        A: 1 (7.69%)
        G: 1 (7.69%)
        H: 1 (7.69%)
        I: 3 (23.08%)
        N: 1 (7.69%)
        R: 1 (7.69%)
        S: 3 (23.08%)
        T: 2 (15.38%)
    
+ hw2/letter.py - module that allows for conversion to/from letter indices 0-25. Can also be used on the command line too:

        $ ./letter.py a b c z word 0 25 14
        a: 0
        b: 1
        c: 2
        z: 25
        w: 22
        o: 14
        r: 17
        d: 3
        0: a
        25: z
        14: o

+ hw3/ - contains automated analysis of linear recurrence and linear
feedback shift registers

+ hw3/vectors.py - a program that finds the period of repetition of
a linear recurrence for all 32 permutations of a 5 bit initialization vector

+ hw3/hankel.py - a program that uses numpy to calculate probable length
of a linear recurrence given a bitstream. It also calculates the coefficients
for the resulting linear recurrence equation. Also contains some functions
for creating hankel matrices.

TODO
------------
At some point I plan to consolidate all the little functions into
a usable package in products. But for now, they are sorted by 
homework assignments, at least until I have time to put them together
into a package.

Also, I don't think I've added hw3/hankel.py. Yet.
