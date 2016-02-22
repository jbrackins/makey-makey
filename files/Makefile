# GNU C/C++ compiler and linker:
LINK = g++

# COMPILER OPTIONS:
CFLAGS = -c  -g -O0
CXXFLAGS = $(CFLAGS) -std=c++11 -Wall

#OBJECT FILES
OBJS = 

#OBJECT FILES FOR TEST PROGRAMS
TESTS = 

#HEADER FILES
HEAD = 

#EXECUTABLES
EXECS = <SKELETON>

all: <SKELETON>

<SKELETON>: src/<SKELETON>.o ${OBJS}
	${LINK} -o $@ $^
doxygen:
	doxygen doc/doxy.conf 
	(cd ./doc/latex && make)
	cp ./doc/latex/refman.pdf doxygen.pdf	
dox:
	make doxygen
clean:
	rm -f *.o *~ core src/*.o inc/*~ src/*~ $(EXECS) *~
#Hahaha I am a bad speller sometimes so let's add these for no reason:
clena:
	make clean
celan:
	make clean
realclean:
	rm -f *.o *~ core src/*.o inc/*~ src/*~ $(EXECS) *~ *.swp
	rm -rf doc/html doc/latex <SKELETON>.tar doxygen.pdf
edit:
	gedit inc/*.h src/*.cpp Makefile &
sublime:
	subl inc/*.h src/*.cpp Makefile &
#ZIP UP ENTIRE ARCHIVE FOR SUBMISSION. GENERATE LATEX PDF AND LET ER GO
archive:
	make realclean
	make doxygen
	tar --exclude='../<SKELETON>/.git' --exclude='../<SKELETON>/doc' -cvf <SKELETON>.tar ../<SKELETON>/
#Don't ask.....
a_better_person:
	@echo ""
	@echo "( ͡° ͜ʖ ͡°)  ﻿ｙｏｕ  ａｒｅ  ａ  ｗｏｎｄｅｒｆｕｌ  ｐｅｒｓｏｎ"
	@echo ""