#ECE2524 Homework 4 Problem 1 Laurin Mordhorst

import argparse
import sys
import fileinput
import operator
import copy
import re

parser = argparse.ArgumentParser(description='Multiply numbers')
parser.add_argument('-f', '--data-file', action='store', dest='datafile')
arguments = parser.parse_args()

lis = list()
dic = dict()
for line in fileinput.input(arguments.datafile):
    if (line != "%%\n"):
        entry = line.split(": ")
        entry[1] = entry[1].rstrip("\n")
        dic[entry[0]]=entry[1]
    else:
        lis.append(dic)
        dic=dict()
                       
def add(lis, command):
    lis.append(command)
    return (lis, "OK")
    
def remove(lis, command):
    return ([tup for tup in lis if tup[command[0]]!=command[1]], "OK")
    
def update(lis, command):
    for dic in lis:
        try:
            if (dic[command[2]] == command[3]):
                dic[command[0]] = command[1]
        except KeyError, kE:
            return (None, "ERROR: Field does not exist.")   
    return (lis, "OK")
     
def list_all(lis):
    for dic in lis:
        for key in dic:
            print(key + ": %s") % dic[key]
        print("%%")
    return (None, "OK")
        
def list_with(lis, command):
    try:
        return list_all([tup for tup in lis if tup[command[0]]==command[1]])
    except KeyError, kE:
        return None, "ERROR: Field does not exist."
        
def list_sorted(lis, command):
    numeric = True
    numericList = list()
    for dic in lis:
        try:
            dicCopy = copy.deepcopy(dic)
            dicCopy[command] = int(dicCopy[command])
            numericList.append(dicCopy)
        except KeyError, kE:
            return(None, "ERROR: Field does not exist.")
        except ValueError, vE:
            numeric = False
            break
    if(numeric == True):
        return list_all(sorted(numericList, key=operator.itemgetter(command)))
    else:
        return list_all(sorted(lis, key=operator.itemgetter(command)))

def write(lis):
    datafile = open(arguments.datafile, 'w')
    datafile.truncate()
    for dic in lis:
        for key in dic:
            datafile.write(key + ": " + dic[key] + "\n")
        datafile.write("%%\n")
    datafile.close()
 
def parse_request(line): 
    pat_add = re.search(r"add {('([\w,-/]+)': ?'([\w ,-/%]+)',? ?)+}", line)
    pat_remove = re.search(r"remove ([\w,-/]+) ?= ?([\w,-/% ]+)", line)
    pat_update = re.search(r"set ([\w,-/]+) ?= ?([\w,-/% ]+) for ([\w,-/]+) ?= ?([\w,-/% ]+)", line) 
    pat_list_all = re.search(r"list all$", line) 
    pat_list_with = re.search(r"list all with ([\w,-/]+) ?= ?([\w,-/% ]+)", line)
    pat_list_sorted = re.search(r"list all sort by ([\w,-/%]+)", line)
    if (pat_add):
        pat_add = re.findall(r"'([\w,-/]+)': ?'([\w,-/% ]*)'", pat_add.group(0))
        addDict = dict()
        for record in pat_add:
            addDict[record[0]] = record[1]
        return add(lis, addDict)               
    if (pat_update):
        return update(lis, [pat_update.group(1), pat_update.group(2), pat_update.group(3), pat_update.group(4)])
    if (pat_remove):
        return remove(lis, [pat_remove.group(1), pat_remove.group(2)])
    if (pat_list_all):
        return list_all(lis)
    if (pat_list_with):
        return list_with(lis, [pat_list_with.group(1), pat_list_with.group(2)])
    if (pat_list_sorted):
        return list_sorted(lis, pat_list_sorted.group(1))
    else:
        return(None, "ERROR: No such command.")
             
while(True):
    try:
        newList, response = parse_request(raw_input())
        if (newList != None):
            lis = newList
        if (response != None):
            print response
    except EOFError:
        write(lis)
        sys.exit(1)
    
