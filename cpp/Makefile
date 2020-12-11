CC = g++

CFLAGS = -g -std=c++17
LINKER =  -L/usr/local/lib -lboost_filesystem -lboost_regex -lboost_system

TARGET = advent

src := $(wildcard *.cc)
headers := $(wildcard *.hh)

main: main.o
	$(CC) $(CFLAGS) $(LINKER) -o main *.o

main.o: $(src) $(src) $(headers)
	$(CC) $(CFLAGS) -c $(src)
