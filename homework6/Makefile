all: generator consumer dispatcher
dispatcher: dispatcher.cpp
	g++ -Wall -g -o dispatcher dispatcher.cpp
generator: generator.cpp
	g++ -Wall -g -o generator generator.cpp
consumer: consumer.cpp
	g++ -Wall -g -o consumer consumer.cpp
clean:
	rm -f *.o *~ *.hh dispatcher generator consumer
