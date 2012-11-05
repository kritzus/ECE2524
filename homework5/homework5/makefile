# ECE 2524: Homework 5 by Laurin Mordhorst (mlaurin1)
CC = g++
CFLAGS = -Wall -g
all: exprtest
exprtest: parser.tab.o scanner.o exprtest.o driver.o
	${CC} ${CFLAGS} -o exprtest exprtest.o driver.o parser.tab.o scanner.o
exprtest.o: exprtest.cpp driver.hpp expression.hpp
	${CC} ${CFLAGS} -c exprtest.cpp
driver.o: driver.cpp driver.hpp scanner.hpp
	${CC} ${CFLAGS} -c driver.cpp
parser.tab.o: parser.tab.cpp expression.hpp parser.tab.hpp driver.hpp scanner.hpp
	${CC} ${CFLAGS} -c parser.tab.cpp
parser.tab.cpp: parser.ypp
	bison parser.ypp
scanner.o: scanner.cpp scanner.hpp
	${CC} ${CFLAGS} -c scanner.cpp
scanner.cpp: scanner.ll
	flex -t scanner.ll > scanner.cpp
clean:
	rm -f *.o *~ *.hh parser.tab* scanner.cpp exprtest core
