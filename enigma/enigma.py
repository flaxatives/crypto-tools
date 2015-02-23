#!/usr/bin/python

def main(messagefile):
    # read the file into array
    # this holds each 6-letter ciphertext starts
    starts = open(messagefile).read().split()

    decompositions = []
    for i in range(3):
        # make a list of unique characters of the i-th position
        # these will be the characters that we haven't found
        # the cycle for yet
        remaining = list(set([word[i] for word in starts]))
        
        print("Chars to find (%i): %s" 
                % (len(remaining), ''.join(remaining))) 
        decomp = []
        # while we have unnaccounted chars, find the cycle
        while len(remaining) > 0:
            print("Finding Cycle starting with: %s" % remaining[0])

            # find the cycle of a remaining char
            cycle = findcycle(i, starts, remaining[0])
            decomp.append(cycle)
            print("Found cycle: %s" % formatcycle(cycle))

            # remove the chars in cycle from remaining
            for char in cycle:
                remaining.remove(char)

            print("Remaining chars: %s" % ''.join(remaining))

        print("Our decomposition is:")
        print(formatdecomp(decomp))
        print('')
        decompositions.append(decomp)

    # done

    finderror(starts)

# finds a single cycle from a list of starts and the starting char
# must have same case, preferably uppercase
def findcycle(i, ciphers, startchar):

    # make a dictionary of char {i : i+3}
    dic = dict([ (word[i], word[i+3]) for word in ciphers ])

    # follow dictionary entries until wraparound
    # back to our first char
    current = first = startchar
    cycle = [first]
    while dic[current] != first:
        cycle.append(dic[current])
        current = dic[current]

    return cycle


# finds errors by creating a dictionary
# then running through the words again for mismatches
def finderror(words):
    for i in range(3):
        # create dictionary
        dic = dict([ (word[i], word[i+3]) for word in words ])

        # check for mismatches
        for word in words:
            if word[i+3] != dic[word[i]]:
                print("Error with %s at %i:%i" % (word, i, i+3))

# put data into readable formats
def formatdecomp(d):
    string = ''
    for cycle in d:
        string += formatcycle(cycle)

    return string.lower()

def formatcycle(cycle):
    return "(%s)" % ''.join(cycle).lower()


if __name__ == "__main__":
    main("messages.txt")
