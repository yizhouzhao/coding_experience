#-*-coding:utf-8-*-
print '\n A Tiny Dictionary for Middle Egyptian (Version-0.2) \n Author: Yizhou \n 12/25/2015 \n'

import sys
import re
try:
    wordframe = {}
    wordframe2 = {}
    writeframe = {}
    wordlist = []
    writinglist = []
    meaninglist = []

    with open('reference\words.txt','r') as f:
        for line in f:
            dic = line.split('&')
            wordlist.append(dic[0])
            writinglist.append(dic[2])
            meaninglist.append(dic[1])

    assert len(writinglist)==len(wordlist)
    assert len(meaninglist)==len(wordlist)


    flag = 'y'
    while flag == 'y' or flag == 'Y':
        print 'Please input your mode: \nif you want to search by pronunciation, input a+Enter;'
        print 'If you want to search by Symbols in Gardiner\'s Classification,input b+Enter.'
        mode = raw_input('input: ')

        if mode == 'a':
            print "Please input the word(or part) you want to find:"

            content = raw_input("word: \n")

            findnum = []
            for i in range(len(wordlist)):
                if content in wordlist[i]:
                    findnum.append(i)

            if len(findnum) == 0:
                print "Nothing found, Please try again"

            else:
                print "%5s %-15s %-30s %-30s" % ("    ","(Pronunciation)", "(Translation)", "(Spelling)")
                for i in range(len(findnum)):
                    print "%5s %-15s %-30s %-30s" % (i, wordlist[findnum[i]],meaninglist[findnum[i]], writinglist[findnum[i]])

            print "Want continue,please input(y/Y),and Press Enter"
            print "Else, Quit"
            flag = raw_input()

        if mode == 'b':
            print '\nDefinitions\nA - Men\nB - Women\nC - Gods\nD - Parts of Men\nE - Mammals\nF - Parts of Mammals\n\
G - Birds\nH - Parts of birds\nI - Reptiles\nK - Fish\nL - Insects\nM - Plants\nN - Sky\nO - Buildings\nP - Boats\nQ - Furniture\n\
R - Temple Furniture and Emblems\nS - Clothing\nT - Warfare and Hunting\nU - Agriculture and Crafts\nV - Rope, Baskets, and Cloth\n\
W - Stone and Ceramic Vessels\nX - Bread\nY - Writing, Games, Music\nZ - Strokes and Figures\nJ - Unclassified\n'
            print 'Please input the Signs of the word you want to find.'
            content = raw_input('Signs:(eg:G X F or N8 G17 G17 or . N35 G1 Z):')
            st = content.split(' ')
            rex = ''
            for i in range(len(st)-1):
                rex += st[i]
                if st[i][-1].isdigit():
                    rex += '\s-\s'
                else:
                    rex += '\d+\s-\s'
            rex += st[-1]
            #rex = '\d+\s-\s'.join(st)

            #print rex
            findnum = []
            for i in range(len(writinglist)):
                if re.search(rex,writinglist[i]):
                    findnum.append(i)

            if len(findnum) == 0:
                print "Nothing found, Please try again"


            else:
                print "%5s %-15s %-30s %-30s" % ("    ","(Pronunciation)", "(Translation)", "(Spelling)")
                for i in range(len(findnum)):
                    print "%5s %-15s %-30s %-30s" % (i, wordlist[findnum[i]],meaninglist[findnum[i]], writinglist[findnum[i]])

            print "Want continue,please input(y/Y),and Press Enter"
            print "Else, Quit"
            flag = raw_input()
except:
    print "Unexpected error:", sys.exc_info()
    raw_input('press enter key to exit')

