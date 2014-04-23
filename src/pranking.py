#!/usr/bin/env

from __future__ import print_function
import subprocess
import urllib2
import re
import ftplib
import datetime
import sys
import getopt
from array import array



class Committer:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        return "self.name: ", self.renderRank, "(", self.count, ")"

    def renderRank(self):
        rank = ""
        for i in range(0, self.count):
            rank += "*"
        return rank

class Ranking:
    def __init__(self, history, period=None, pretty=False):
        self.history = history
        self.period = period
        self.pretty = pretty

    def buildRanking(self):
        #Extract all the commit authors
        res=dict()
        sep = re.split("\n", self.history)
        for s in sep:
            m = re.search('Author:(.*)<.*>', s)
            if(m):
                res[m.group(1)] = m.group(1)
                
        commiters=dict()
        #Build the committers
        for r in res:        
            if self.period == None:
                #grep output is piped to cat because a zero-match grep
                #returns a non-zero status and crashes this call
                count = int(subprocess.check_output("git log | grep -c \"" + r + "\" | cat", shell=True))
            else:
                date = str(datetime.date.today()+datetime.timedelta(-(self.period)))
                count = int(subprocess.check_output("git log --since=\"" + date + "\" | grep -c \"" + r + "\" | cat", shell=True))
            commiters[r] = Committer(r, count)
                
        #Sort according to rank
        tipos = sorted(commiters.values(), reverse=True, key=lambda guy: guy.count)
            
        #This helps format the output
        maxLength = 0
        for t in tipos:
            if len(t.name) > maxLength:
                maxLength = len(t.name)
                    
        #Add the committers
        i=1
        choricillo = ""
        for t in tipos:
            form = "{:<" + str(maxLength+5) + "}"
            name = form.format(t.name)
            commits = str(t.count)
            balls = str(t.renderRank())
            choricillo += str(i) + ". " + name
            if self.pretty:
                choricillo += "\n" + balls
                commits = "(" + commits + ")"
            choricillo +=  commits + "\n"
            i+=1
                            
        return choricillo
                        

def main(argv):

    days = None
    pretty = False
    try:
        opts, args = getopt.getopt(argv,"t:p",["time=", "pretty"])
    except getopt.GetoptError:
        printUsage()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-t", "--days"):
            days = int(arg)
            if days < 0:
                printUsage()
                sys.exit(2)
        elif opt in ("-p", "--pretty"):
            pretty = True
                
    #Get commit history 
    history = subprocess.check_output("git log | grep -i \"author\" | cat", shell=True)

    rank = Ranking(history, days, pretty)
        
    msgContent = rank.buildRanking()
    
    print(msgContent)


def printUsage():
    print("\n")
    print("\033[1mUsage:\033[0m python rank.py [OPTIONS]")
    print("\n")
    print("\033[1mOPTIONS\033[0m:")
    print("\t-t \033[4mDAYS\033[0m, --time=\033[4mDAYS\033[0m \n\t\tOnly commits from the last \033[4mDAYS\033[0m days are considered. \033[4mDAYS\033[0m must be a positive integer.")
    print("\n")
    print("\t-p, --pretty \n\t\tA string of as many asterisks as commits correspond to the Author will be printed.")
    print("\n")

if __name__ == "__main__":
   main(sys.argv[1:])
