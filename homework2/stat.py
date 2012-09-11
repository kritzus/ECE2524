# ECE 2524 Homework 2 Problem 3 Laurin Mordhorst
sum_all = 0.0
i = 0
minimum = float("inf")
maximum = float("-inf")
print "ACCOUNT SUMMARY"
with open('account', 'r') as f:
    for line in f:
        i += 1
        line = line.split()
        balance = float(line[2])
        if balance < minimum:
            minimum = balance
            minimum_name = line[1]
        if balance > maximum:
            maximum = balance
            maximum_name = line[1]
        sum_all += balance
    average = sum_all / i
    print "Total amount owed = %.2f" %sum_all
    print "Average amount owed = %.2f" %average
    print "Maximum amount owed = %.2f owned by %s" %(maximum, maximum_name)
    print "Minimum amount owed = %.2f owned by %s" %(minimum, minimum_name)
