# ECE 2524 Homework 2 Problem 1 Laurin Mordhorst
with open('/etc/passwd', 'r') as f:
    for line in f:
        line = line.split(':')
        print line[0].rstrip() + "\t" + line[5].rstrip()
