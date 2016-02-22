#!/usr/bin/python3

import sys
import datetime
from subprocess import call

# ===========================================================================
# Replacer Class
# ===========================================================================

class Replacer(object):

    def __init__( self, proj ):
        #Config File
        self.CONFIG = "renamer.conf"

        #General Stuff
        self.AUTHOR_NAME       = None
        self.CURRENT_DATE              = None
        self.PROJECT_NAME      = proj
        self.PROJECT_NAME_CAPS = proj.upper()

        #Course Information
        self.COURSE_NAME     = None
        self.COURSE_SECTION  = None
        self.COURSE_LOCATION = None
        self.PROFESSOR_NAME  = None
        
        #Value you are replacing
        self.OLD      = "<SKELETON>"
        self.OLD_CAPS = "<SKELETON_CAPS>"

    def setDate( self ):
        self.CURRENT_DATE = datetime.datetime.today().strftime('%B %d, %Y')

    def readConfig( self ):
        with open(self.CONFIG, "r") as ins:
            array = []
            for line in ins:
                if( line[0] != "#" and line[0] != "\n" ):
                    array.append(line)

        for input_line in array:
            pair = input_line.split('=', 1 )
            key = pair[0].strip()
            value = pair[1].strip()
            value = value.strip('\n')
            print(key,value)

            if(key=="AUTHOR_NAME"):
                self.AUTHOR_NAME = value
            elif(key=='COURSE_NAME'):
                self.COURSE_NAME = value
            elif(key=='COURSE_SECTION'):
                self.COURSE_SECTION = value
            elif(key=='COURSE_LOCATION'):
                self.COURSE_LOCATION = value
            elif(key=='PROFESSOR_NAME'):
                self.PROFESSOR_NAME = value

    def makeTemp( self, infile, outfile ):
        call(["cp", infile, outfile])

    def swap( self, file, old, new ):
        f = open(file,'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(old,new)

        f = open(file,'w')
        f.write(newdata)
        f.close()


def replace( old, new ):
    print("replacing", old, "with", new)

def usage( args ):
    usage = "Usage: " + args[0] + " <filename>\n"
    usage = usage + "<projectname> - New project name"
    return usage

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print( usage( sys.argv ) )
    else:
        r = Replacer(sys.argv[1])
        r.readConfig()
        r.setDate()

        #Rewrite the .cpp file
        ifile = "files/SKELETON.cpp"
        ofile = "temp/temp.cpp"
        r.makeTemp(ifile, ofile)

        r.swap(ofile, "<SKELETON>", r.PROJECT_NAME)
        r.swap(ofile, "<SKELETON_CAPS>", r.PROJECT_NAME_CAPS)
        r.swap(ofile, "<AUTHOR_NAME>", r.AUTHOR_NAME)
        r.swap(ofile, "<CURRENT_DATE>", r.CURRENT_DATE)
        r.swap(ofile, "<COURSE_NAME>", r.COURSE_NAME)
        r.swap(ofile, "<COURSE_SECTION>", r.COURSE_SECTION)
        r.swap(ofile, "<COURSE_LOCATION>", r.COURSE_LOCATION)
        r.swap(ofile, "<PROFESSOR_NAME>", r.PROFESSOR_NAME)

        #Rewrite the .h file
        ifile = "files/SKELETON.h"
        ofile = "temp/temp.h"
        r.makeTemp(ifile, ofile)

        r.swap(ofile, "<SKELETON>", r.PROJECT_NAME)
        r.swap(ofile, "<SKELETON_CAPS>", r.PROJECT_NAME_CAPS)
        r.swap(ofile, "<AUTHOR_NAME>", r.AUTHOR_NAME)
        r.swap(ofile, "<CURRENT_DATE>", r.CURRENT_DATE)
        r.swap(ofile, "<COURSE_NAME>", r.COURSE_NAME)
        r.swap(ofile, "<COURSE_SECTION>", r.COURSE_SECTION)
        r.swap(ofile, "<COURSE_LOCATION>", r.COURSE_LOCATION)
        r.swap(ofile, "<PROFESSOR_NAME>", r.PROFESSOR_NAME)

        #Rewrite the Makefile
        ifile = "files/Makefile"
        ofile = "temp/tempMakefile"
        r.makeTemp(ifile, ofile)

        r.swap(ofile, "<SKELETON>", r.PROJECT_NAME)
        r.swap(ofile, "<SKELETON_CAPS>", r.PROJECT_NAME_CAPS)
        r.swap(ofile, "<AUTHOR_NAME>", r.AUTHOR_NAME)
        r.swap(ofile, "<CURRENT_DATE>", r.CURRENT_DATE)
        r.swap(ofile, "<COURSE_NAME>", r.COURSE_NAME)
        r.swap(ofile, "<COURSE_SECTION>", r.COURSE_SECTION)
        r.swap(ofile, "<COURSE_LOCATION>", r.COURSE_LOCATION)
        r.swap(ofile, "<PROFESSOR_NAME>", r.PROFESSOR_NAME)

        #Rewrite the .conf file
        ifile = "files/SKELETON.conf"
        ofile = "temp/temp.conf"
        r.makeTemp(ifile, ofile)

        r.swap(ofile, "<SKELETON>", r.PROJECT_NAME)
        r.swap(ofile, "<SKELETON_CAPS>", r.PROJECT_NAME_CAPS)
        r.swap(ofile, "<AUTHOR_NAME>", r.AUTHOR_NAME)
        r.swap(ofile, "<CURRENT_DATE>", r.CURRENT_DATE)
        r.swap(ofile, "<COURSE_NAME>", r.COURSE_NAME)
        r.swap(ofile, "<COURSE_SECTION>", r.COURSE_SECTION)
        r.swap(ofile, "<COURSE_LOCATION>", r.COURSE_LOCATION)
        r.swap(ofile, "<PROFESSOR_NAME>", r.PROFESSOR_NAME)        