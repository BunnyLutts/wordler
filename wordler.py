import json

from more_itertools import countable

words = []
pos_words = []
ava_words = []
target_len = 0

def readDict(name):
    with open(name) as f:
        for i in f:
            words.append(i.strip())

def init(length):
    global target_len, pos_words, ava_words
    target_len = length
    pos_words = list(filter(lambda x : len(x)==length, words))
    ava_words = pos_words

def satisfy(msg, word):
    for i in range(target_len):
        if (msg[2*i+1]=='0'):
            if (msg[2*i] in word):
                return False
        elif msg[2*i+1]=='1':
            if (not msg[2*i] in word) or word[i] == msg[2*i]:
                return False
        else:
            if msg[2*i]!=word[i]:
                return False
    return True

def compareWord(hyp, ref):
    msg = ""
    for i in range(target_len):
        msg += hyp[i]
        if (hyp[i] == ref[i]):
            msg += '2'
        elif (hyp[i] in ref):
            msg += '1'
        else:
            msg += '0'
    return msg

def countPos(word):
    count = dict()
    for i in pos_words:
        msg = compareWord(word, i)
        if (msg not in count):
            count[msg] = 0
        count[msg] += 1
    sum = 0
    for v in count.values():
        sum += v*v
    return sum/len(pos_words)

def guess():
    min_poss = len(pos_words)
    min_word = pos_words[0]
    for wi in ava_words:
        now_poss = countPos(wi)
        if (now_poss < min_poss):
            min_poss = now_poss
            min_word = wi
    return min_word

def runGame():
    global pos_words, ava_words
    length = int(input('Input the length of the word: '))
    init(length)
    HELP_MSG = '''
Each time the program will guess a word.
Input the results of the guess in the following format:
a0b1c2d0e1
0 means the former letter doesn't exist in the word,
1 means the former letter exists in the word but not at the right position,
2 means the former letter exists in the word and at the right position.
Input a line with only 'q' to quit the game.
    '''
    print(HELP_MSG)
    while True:
        try:
            print(guess())
        except Exception as e:
            print('Guess skipped.')
        msg = input('Result:')
        if (msg=='q'):
            return
        pos_words = list(filter(lambda x : satisfy(msg, x), pos_words))
        if (len(pos_words)==0):
            print("No word can be found.")
            return
        elif (len(pos_words)==1):
            print("Find word:", pos_words[0])
            return

def main():
    readDict("wordle.txt")
    while True:
        runGame()

if __name__ == "__main__":
    main()