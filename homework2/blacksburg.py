# ECE 2524 Homework 2 Problem 2 Laurin Mordhorst
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open('account', 'r') as f:
    for line in f:
        line = line.split();
        if line[3] == "Blacksburg":
            print line[4] + ", " + line[1] + ", " + line[0] + ", " + line[2]
